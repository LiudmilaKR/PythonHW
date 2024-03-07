'''
Создайте функцию генератор чисел Фибоначчи
'''


def gen_fibs(n: int):
    number1, number2 = 0, 1
    for _ in range(n):
        number = number1 + number2
        number1 = number2
        number2 = number
        yield number


def gen_fib1():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for i in gen_fibs(25):
        print(i, end=' ')

# создаем генератор чисел
    fib = gen_fib1()