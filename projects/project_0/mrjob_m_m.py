from mrjob.job import MRJob
from mrjob.step import MRStep
import logging


class MR_mat_mat(MRJob):

    def __init__(self, args=None):
        super().__init__(args)
    def configure_args(self):
        """
        dadurch wird das programm wie folgt aufgerufen:
        python3 mrjob_m_m.py --matrix-dimensions '1000,1000' input.txt
        """
        super().configure_args()  # call the super class method
        self.add_passthru_arg('--matrix-dimensions', type=str, default='1000,1000',
                              help='Dimensions of the matrices as N,M')

    def mapper(self, key, input):
        """
        line = i(zeile) j(spalte) value mat_name
        """
        matrix_dimensions = self.options.matrix_dimensions.split(',')
        N, M = map(int, matrix_dimensions)
        current_line = input.split()
        # überspringe werte die 0 sind
        # if current_line[2] == '0':
        #     pass
        # else:
        if current_line[3] == "A":
            # d.h wir haben einen Eintrag der Matrix A(zeile, spalte, wert, "A")
            for j in range(0, M):
                # d.h wir geben hier key = (i ,j) und value = (i, j, wert, "A") aus
                yield (int(current_line[0]), j), (int(current_line[0]),int(current_line[1]), int(current_line[2]), "A")
        if current_line[3] == "B":
            # d.h wir haben einen Eintrag der Matrix B(zeile, spalte, wert, "B")
            for i in range(0, N):
                # d.h wir geben hier key = (i ,j) und value = (i, j, wert, "B") aus
                yield (i, int(current_line[1])), (int(current_line[0]),int(current_line[1]), int(current_line[2]), "B")

    def reducer(self, key, values):
        # key = (i, j), values = [(i, j, wert, "A"), (i, j, wert, "B")]
        # sortiere die values nach dem 4. Eintrag (A oder B)
        A = {}
        B = {}
        for value in values:
            if value[3] == "A":
                A[(value[0],value[1])] = value[2]
            if value[3] == "B":
                B[(value[0],value[1])] = value[2]
        # jetzt haben wir zwei dicts mit den Einträgen der Matrix A und B
        result = 0
        for x in range(0, len(A)):
            #bzw. C_i,j = sum(A_i,k * B_k,j)
            result += A.get((key[0],x)) * B.get((x,key[1]))

        yield key, result


if __name__ == '__main__':
    MR_mat_mat.run()