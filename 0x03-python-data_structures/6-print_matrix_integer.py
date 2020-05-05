#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if (matrix[0] == []):
            print()
    
    for i in range(len(matrix)):
        m_len = len(matrix[i])
        for j in range(m_len):
            if (j < (m_len - 1)):
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
