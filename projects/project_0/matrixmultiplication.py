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
        self.add_passthru_arg('--dim', type=str, default='1000,1000',
                              help='Dimensions of the matrices as N,M')

    def mapper(self, key, line):
        """
        line = i(row) j(col) value mat_name
        """
        matrix_dimensions = self.options.dim.split(',')
        n, m = map(int, matrix_dimensions)
        current_line = line.split()
        if current_line[2] == "0.0":
            pass
        if current_line[3] == "A":
            for j in range(0, m):
                # we yield key = (i ,j) value = (i, j, value, "A")
                yield (int(current_line[0]), j), (int(current_line[0]), int(current_line[1]), float(current_line[2]), "A")
        if current_line[3] == "B":
            for i in range(0, n):
                # we yield key = (i ,j) value = (i, j, value, "B")
                yield (i, int(current_line[1])), (int(current_line[0]), int(current_line[1]), float(current_line[2]), "B")

    def reducer(self, key, values):
        # key = (i, j), values = [(i, j, value, "A"), (i, j, value, "b")]
        # sort the values for a and b
        a = {}
        b = {}
        for value in values:
            if value[3] == "A":
                a[(value[0], value[1])] = value[2]
            if value[3] == "B":
                b[(value[0], value[1])] = value[2]
        # now we have two dictionaries with the values of a and b
        result = 0
        for x in range(0, len(a)):
            # bzw. C_i,j = sum(A_i,k * B_k,j)
            value_a = a.get((key[0], x))
            value_b = b.get((x, key[1]))
            result = 0
            if value_a is not None and value_b is not None:
                result += value_a * value_b

        yield key, result


if __name__ == '__main__':
    """
    python3 matrixmultiplication.py input_100x100.txt --runner=local --jobconf mapreduce.job.maps=100 --jobconf mapreduce.job.reduces=100 > output.txt
    """
    MatrixMultiplication.run()
