'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_NUMBER = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

count = 0
while True:
    count += 1
    my_attemp = int(input('Введите вариант загаданного числа => '))
    if my_attemp == num:
        print(f'Вы угадали, загаданное число, действительно {my_attemp}.')
        break
    elif count == ATTEMPT_NUMBER:
        print(f'К сожалению, это была последняя {ATTEMPT_NUMBER} попытка.')
        break
    elif my_attemp < num:
        print(f'{my_attemp} - не угадали, попробуйте число побольше.')
    elif my_attemp > num:
        print(f'{my_attemp} - не угадали, попробуйте число поменьше.')
        