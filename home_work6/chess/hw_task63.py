'''
Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

from random import randint

def gen_pairs(n: int) -> list:
    set_pairs = set()
    while len(set_pairs) < n:
        set_pairs.add((randint(1, 8), randint(1, 8)))
    return set_pairs


if __name__ == '__main__':
    print(gen_pairs(8))
        