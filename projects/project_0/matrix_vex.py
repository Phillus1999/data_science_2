from mrjob.job import MRJob

class MRMatrixVex(MRJob):
    def mapper(self, key, line):
        line = line.split()
        if len(line) == 3:
            zeile, spalte, wert = int(line[0]), int(line[1]), float(line[2])
            yield zeile, ('mat', spalte, wert)
        else:
            zeile, wert = int(line[0]), float(line[1])
            # range ist die Anzahl der Spalten
            for spalte in range(3):
                yield spalte, ('vec', zeile, wert)


    def reducer(self, key, values):
        vec = []
        mat = []
        for value in values:
            if value[0] == 'vec':
                vec.append(value[2])
            else:
                mat.append(value[2])

        res = 0
        for i in range(len(vec)):
            res += float(vec[i]) * float(mat[i])

        yield key, res

if __name__ == '__main__':
    MRMatrixVex.run()
