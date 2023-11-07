from mrjob.job import MRJob

"""
Da die Texte die wird im Datensatz betrachten, relativ klein sind, betrachten wir Character anstatt Strings (Wörter)
als Shingles. 

Deshalb reicht die Länge k=3 völlig aus.
Wir nehmen kein K=2, weil, wenn es zuviele "kleine" Shingles gibt, werden Ähnlichkeiten angeommen, die es gar nicht gibt.

Die Whitespaces werden mit betrachtet, da sie nicht in der Analyse relevant sind, weil sie bei der Bestimmung der Ähnlichkeit
keine Rolle spielen. 

"""


class ShinglesCount(MRJob):

    def mapper(self, _, line):
        """
        Erstellt Shingles der Länge k (default=3) aus einer Zeile.
        :param line: Eine Zeile.
        :return: Generator der Shingles
        """
        elements = line.strip().split('\t')
        texts = elements[0:2]
        k = 3
        for text in texts:
            # erstelle die Shingles
            for i in range(len(text) - k + 1):
                yield text[i:i + k], 1

    def reducer(self, shingle, counts):
        """
        :param shingle (Key):
        :param counts (Value):
        :return:
        """
        yield shingle, sum(counts)


if __name__ == '__main__':
    ShinglesCount.run()
