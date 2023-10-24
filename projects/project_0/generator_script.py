import numpy as np
from scipy.sparse import random

def convert_matrix(matrix, name):
    """
    Converts a matrix into a list of (i, j, value, name) tuples.
    return: converted: list of (i, j, value, name) tuples
    """
    converted = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            converted.append([i, j, value, name])

    return converted


def calculate_result(matrix_A, matrix_B):
    """
    Calculates the dot product of two matrices.
    return: result: dot product of matrix_A and matrix_B as np.array
    """
    a = np.array(matrix_A)
    b = np.array(matrix_B)
    return np.dot(a, b)


def write_file(matrix, filename):
    """
    Writes a matrix into a file.
    """
    with open(filename, 'w') as file_obj:
        for row in matrix:
            for column in row:
                file_obj.write(str(column) + ' ')
            file_obj.write("\n")


def create_scenario(scenario_name, size_a=(100, 100), size_b=(100, 100)):
    """
    param: scenario_name: name of the scenario
    param: size_a: size of matrix A -> tuple (rows, columns)
    param: size_b: size of matrix B -> tuple (rows, columns)
    Creates all files for the matrix-matrix multiplication.
    1st file: input_scenario_name.txt
    2nd file: result_scenario_name.txt
    """
    # create matrix
    matrix_a = random(size_a[0], size_a[1], density=0.01).toarray()
    matrix_b = random(size_b[0], size_b[1], density=0.01).toarray()
    # convert matrix
    matrix_list_a = convert_matrix(matrix_a, "A")
    matrix_list_b = convert_matrix(matrix_b, "B")
    result_matrix_list = convert_matrix(calculate_result(matrix_a, matrix_b), "C")
    # write files
    input_data = matrix_list_a + matrix_list_b
    write_file(input_data, "input_" + scenario_name + ".txt")
    write_file(result_matrix_list, "result_" + scenario_name + ".txt")


def clear_all_txt():
    """
    Deletes all .txt files in the current directory.
    """
    import os
    for file in os.listdir():
        if file.endswith(".txt"):
            os.remove(file)


if __name__ == '__main__':

    clear_all_txt()
    create_scenario("100x100")