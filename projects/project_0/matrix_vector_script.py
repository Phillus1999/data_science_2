import numpy as np


def convert_matrix(matrix, name):
    """
    Converts a matrix into a list of (i, j, value) tuples.
    return: converted: list of (i, j, value) tuples
    """
    converted = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            converted.append([i, j, value, name])

    return converted


def convert_vector(vector):
    """
    Converts a vector into a list of (i, value) tuples.
    return: converted: list of (i, value) tuples
    """
    converted = []

    for i, row in enumerate(vector):
        for value in row:
            converted.append([i, value])

    return converted


def calculate_result(matrix_A, matrix_B):
    """
    Calculates the dot product of two matrices.
    param: matrix_A: some matrix
    param: matrix_B: some matrix or vector
    return: result: dot product of matrix_A and matrix_B as np.array
    """
    A = np.array(matrix_A)
    B = np.array(matrix_B)
    return np.dot(A, B)

def write_file(matrix, filename):
    with open(filename, 'w') as file_obj:
        for row in matrix:
            for column in row:
                file_obj.write(str(column) + ' ')
            file_obj.write("\n")

#def write_input_file(matrix_list, vector_list):
#    with open("input.txt", 'w') as input_obj:
#        for row in matrix_list:
#            for column in row:
#                input_obj.write(str(column) + ' ')
#            input_obj.write("\n")
#
#        for row in vector_list:
#            for column in row:
#                input_obj.write(str(column) + ' ')
#            input_obj.write("\n")


# def write_result_file(result):
#    with open("result.txt", "w") as result_obj:
#        result_obj.write(str(result))

def create_scenario_mat_mat(scenario_name, size_a = (1000,1000), size_b=(1000,1000)):
    """
    param: scenario_name: name of the scenario
    param: size_a: size of matrix A -> tuple (rows, columns)
    param: size_b: size of matrix B -> tuple (rows, columns)
    Creates all files for the matrix-matrix multiplication.
    1st file: matrix_a_scenario_name.txt
    2nd file: matrix_b_scenario_name.txt
    3rd file: result_scenario_name.txt
    """
    #create matrix
    matrix_a = np.random.randint(0, 3, size=size_a)
    matrix_b = np.random.randint(0, 3, size=size_b)
    #convert matrix
    matrix_list_a = convert_matrix(matrix_a, "A")
    matrix_list_b = convert_matrix(matrix_b, "B")
    result_matrix_list = convert_matrix(calculate_result(matrix_a, matrix_b), "C")
    #write files
    input = matrix_list_a + matrix_list_b
    write_file(input, "input_" + scenario_name + ".txt")
    write_file(result_matrix_list, "result_" + scenario_name + ".txt")


def create_scenario_mat_vec(scenario_name, size_a = (1000,1000), size_b=(1000,1)):
    """
    param: scenario_name: name of the scenario
    param: size_a: size of matrix -> tuple (rows, columns)
    param: size_b: size of vector -> tuple (rows, columns)
    Creates all files for the matrix-vector multiplication.
    1st file: matrix_scenario_name.txt
    2nd file: vector_scenario_name.txt
    3rd file: result_scenario_name.txt
    """
    #create matrix
    matrix = np.random.randint(0, 3, size=size_a)
    vector = np.random.randint(0, 3, size=size_b)
    #convert matrix
    matrix_list = convert_matrix(matrix)
    vector_list = convert_vector(vector)
    result_matrix_list = convert_vector(calculate_result(matrix, vector))
    #write files
    input = matrix_list + vector_list
    write_file(input, "input_" + scenario_name + ".txt")
    write_file(result_matrix_list, "result_" + scenario_name + ".txt")


def clear_all_txt():
    """
    Deletes all txt files in the current directory.
    """
    import os
    for file in os.listdir():
        if file.endswith(".txt"):
            os.remove(file)

if __name__ == '__main__':

    clear_all_txt()
    create_scenario_mat_mat("1000x1000")