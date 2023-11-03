from mrjob.job import MRJob


class ShinglesCount(MRJob):

    def mapper(self, _, line):
        """
        Erstellt Shingles der Länge k (default=3) aus einer Zeile.
        :param line: Eine Zeile.
        :return: Generator der Shingles
        """
        k = 3
        for i in range(len(line) - k + 1):
            yield line[i:i + k], 1

    def reducer(self, shingle, counts):
        """
        :param shingle (Key):
        :param counts (Value):
        :return:
        """
        yield shingle, sum(counts)