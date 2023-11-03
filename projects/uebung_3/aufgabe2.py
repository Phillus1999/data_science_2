from mrjob.job import MRJob


class ShinglesCount(MRJob):

    def mapper(self, _, line):
        """
        Erstellt Shingles der Länge k (default=3) aus einer Zeile.
        :param line: Eine Zeile.
        :return: Generator der Shingles
        """
        # Hier generieren Sie die k-Shingles
        k = 3  # Setzen Sie k auf den gewünschten Shingle-Wert
        for i in range(len(line) - k + 1):
            yield line[i:i + k], 1