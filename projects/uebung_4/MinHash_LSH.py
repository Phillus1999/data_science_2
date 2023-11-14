import random
from mrjob.job import MRJob
from mrjob.step import MRStep
from sympy import nextprime
import numpy as np


def create_hashfunctions(num_hashfunctions=500):
    hashfunctions = []
    p = nextprime(1000000000)
    while len(hashfunctions) < num_hashfunctions:
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        hashfunctions.append((a, b, p))
    return hashfunctions


def get_shingles(text, k=3):
    return set(text[i:i + k] for i in range(len(text) - k + 1))


class MinHash(MRJob):

    random.seed(47)
    hashfunctions = create_hashfunctions()
    universe_dimension = 50000000    # 50 million some big number
    bands = 50

    def get_bit_vector(self, shingles):
        vector = dict()
        for shingle in shingles:
            hash_value = hash(shingle) % self.universe_dimension
            vector[hash_value] = 1
        return vector

    def get_signature(self, text):
        shingles = get_shingles(text)
        bit_vector = self.get_bit_vector(shingles)
        signature = []
        for a, b, p in self.hashfunctions:
            # berechne den minhash für die aktuelle hash-funktion
            minhash = np.inf
            for hash_value in bit_vector.keys():
                minhash = min(minhash, (a * hash_value + b) % p) % self.universe_dimension
            signature.append(minhash)
        return signature

    def MinHashMapper(self, _, line):
        for text in line.split('\t')[0:2]:
            yield text, self.get_signature(text)

    def MinHashReducer(self, text, values):
        yield text, list(values)[0]

    def LSHMapper(self, text, signature):
        rows = len(signature) // self.bands
        for i in range(self.bands):
            sig_vec = list(signature)
            band = str(sig_vec[i * rows:(i + 1) * rows])
            hash_value = hash(band) % 5054987
            yield hash_value, text

    def LSHReducer(self, key, value):
        values = [element for element in list(value)]
        if len(values) > 1:
            yield key, values

    def LSH_Canditate_Mapper(self, key, value):
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                yield (value[i], value[j]), 1

    def LSH_Jaccard_reducer(self, key, value):
        shingles1 = get_shingles(key[0])
        shingles2 = get_shingles(key[1])
        jaccard = len(shingles1.intersection(shingles2)) / len(shingles1.union(shingles2))
        yield key, jaccard

    def steps(self):
        return [
            MRStep(mapper=self.MinHashMapper, reducer=self.MinHashReducer),
            MRStep(mapper=self.LSHMapper, reducer=self.LSHReducer),
            MRStep(mapper=self.LSH_Canditate_Mapper, reducer=self.LSH_Jaccard_reducer)
        ]

if __name__ == '__main__':
    MinHash.run()