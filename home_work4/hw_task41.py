'''
Напишите функцию для транспонирования матрицы
'''

import numpy as np


def transpose_matrix(matr: list) -> list:
    t_matrix = []
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            break
    
    
if __name__ == '__main__':
    my_matrix = [[0, 1, 2], [3, 4, 5]]
    print(transpose_matrix(my_matrix))

# проверка
my_matrix1 = np.array(range(6)).reshape(2, -1)
t_matrix1 = np.transpose(my_matrix1)
# print(my_matrix)
print(my_matrix1, t_matrix1, sep='\n\n')