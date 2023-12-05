from mrjob.job import MRJob
import numpy as np
import ast
class RankMR(MRJob):
    def mapper(self, _, line):
        data = line.split('\t')
        cat1, cat2 = ast.literal_eval(data[0])
        yield cat1, (cat2, float(data[1]))

    def reducer(self, key, values):
        yield key, list(values)