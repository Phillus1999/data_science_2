from mrjob.job import MRJob


class MatrixMultiplication(MRJob):
    """
    This class implements the matrix multiplication algorithm
    as additional argument it takes the dimensions of the matrices as --dim N,M
    default is 100,100
    """
    def __init__(self, args=None):
        super().__init__(args)

    def configure_args(self):
        """Additional configuration flag for the matrix dimensions"""
        super().configure_args()
        self.add_passthru_arg('--dim', type=str, default='100,100',
                              help='Dimensions of the matrices as N,M')

    def mapper(self, key, line):
        # set the dimensions of the matrices
        matrix_dimensions = self.options.dim.split(',')
        n, m = map(int, matrix_dimensions)
        # parse the input line
        i, j, value, mat_name = line.split()
        i, j, value = int(i), int(j), float(value)
        # ignore zero values
        if value == 0.0:
            pass
        if mat_name == "A":
            for col in range(m):
                yield (i, col), ("A", j, value)
        elif mat_name == "B":
            for row in range(n):
                yield (row, j), ("B", i, value)

    def reducer(self, key, values):
        a_values = dict()
        b_values = dict()

        for mat_name, idx, value in values:
            if mat_name == "A":
                a_values[idx] = value
            else:
                b_values[idx] = value

        result = sum(a_values[k] * b_values.get(k, 0) for k in a_values.keys())
        yield key, result

if __name__ == '__main__':
    """
    execute with: python3 matrixmultiplication.py input_100x100.txt > output.txt
    """
    MatrixMultiplication.run()

