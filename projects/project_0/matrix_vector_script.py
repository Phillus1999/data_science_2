import numpy as np
def convert_matrix(matrix):
    converted = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            converted.append([i, j, value])

    return converted


def convert_vector(vector):
    converted = []

    for i, row in enumerate(vector):
        for value in row:
            converted.append([i, value])

    return converted

# als matrix_B kann auch ein Vektor übergeben werden!
def calculate_result(matrix_A, matrix_B):
    A = np.array(matrix_A)
    B = np.array(matrix_B)

    return np.dot(A, B)
def write_input_file(matrix_list, vector_list):
    with open("input.txt", 'w') as input_obj:
        for row in matrix_list:
            for column in row:
                input_obj.write(str(column) + ' ')
            input_obj.write("\n")

        for row in vector_list:
            for column in row:
                input_obj.write(str(column) + ' ')
            input_obj.write("\n")

def write_result_file(result):
    with open("result.txt", "w") as result_obj:
        result_obj.write(str(result))


if __name__ == '__main__':
    matrix = [[2, 2, 0], [2, -1, -3], [1, 0, 1]]
    vector = [[3], [1], [0]]

    matrix_result = convert_matrix(matrix)
    vector_result = convert_vector(vector)

    result = calculate_result(matrix, vector)

    write_input_file(matrix_result, vector_result)
    write_result_file(result)

