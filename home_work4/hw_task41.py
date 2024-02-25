'''
Напишите функцию для транспонирования матрицы
'''

import numpy as np


def transpose_matrix(matr: list) -> list:
    """_summary_ Function to transpose matrix

    Args:
        matr (list): _description_ matrix

    Returns:
        list: _description_ transposed matrix
    """
    t_matrix = []
    for i in range(len(matr[0])):
        t_matrix_i = []
        for j in range(len(matr)):
            t_matrix_i.append(matr[j][i])
        t_matrix.append(t_matrix_i)
    return t_matrix
    
    
if __name__ == '__main__':
    my_matrix = [[0, 1, 2], [3, 4, 5]]
    print(transpose_matrix(my_matrix))

    # проверка
    print()
    my_matrix1 = np.array(range(6)).reshape(2, -1)
    t_matrix1 = np.transpose(my_matrix1)
    # print(my_matrix)
    print(my_matrix1, t_matrix1, sep='\n\n')
