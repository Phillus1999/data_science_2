from mrjob.job import MRJob
from mrjob.step import MRStep


class MR_mat_mat(MRJob):

    def configure_args(self):
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
        # skip 0 values
        if current_line[2] == 0:
            pass
        else:
            # matrix A
            if current_line[3] == "A":
                for x in 1000:
                    (i,x) + val
            # matrix B
            elif current_line[3] == "B":
                for y in 1000:
                    (y,j) + val


    def reducer(self, key, values):
        # key = (i,j)       value("A"oder"B", zellenwert)
        # (i,j) ist der Schlüssel, also die Position des Eintrags in der Zielmatrix
        # Die Werte sind alle Einträge der Matrix A in der i-ten Zeile
        # und alle Werte der Matrix B in der j-ten Spalte
        matrix_dimensions = self.options.matrix_dimensions.split(',')
        N, M = map(int, matrix_dimensions)
        res = 0
        for x in range(0,M):
            res += A[i][x] * B[x][j]


        yield (i,j), res

if __name__ == '__main__':
    MR_mat_mat.run()