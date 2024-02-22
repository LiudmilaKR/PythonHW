'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
'''

num10 = int(input('Введите целое число => '))

num16 = ''
temp = num10
while num10 / 16 > 0:
    simb = str(num10 % 16)
    match simb:
        case '10':
            simb = 'A'
        case '11':
            simb = 'B'
        case '12':
            simb = 'C'
        case '13':
            simb = 'D'
        case '14':
            simb = 'E'
        case '15':
            simb = 'F'
    num16 = simb + num16
    num10 //= 16

print(f'Число {temp} в шестнадцатеричном представлении - {"0x" + num16}')
print('Check:')
print(f'Число {temp} в шестнадцатеричном представлении - {hex(temp)}')