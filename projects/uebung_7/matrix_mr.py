from mrjob.job import MRJob
import json
import numpy as np


class MatrixMR(MRJob):
    def mapper(self, _, line):
        data = json.loads(line)
        categories = data['categories'].split(' ')
        # yield all possible pairs of categories
        for i in range(len(categories)):
            for j in range(i+1, len(categories)):
                yield categories[i], categories[j]

    def reducer(self, key, values):
        # get len of all values
        values = list(values)
        length = len(values)
        # get all value counts
        categories, counts = np.unique(values, return_counts=True)
        for cat, count in zip(categories, counts):
            weight = count / length
            yield (key, cat), weight
