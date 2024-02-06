'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

HIGH_LIMIT = 100000

while True:
    num = int(input('Введите положительное число => '))
    if num < 0 or num > HIGH_LIMIT:
        print(f'Число должно быть положительным и меньше {HIGH_LIMIT}!')
    else:
        break

if num == 1 or num % 2 == 0:
    print(f'Число {num} не является простым.')
elif num == 3:
    print(f'Число {num} - простое.')
else:
    for i in range(3, num, 2):
        if num % i == 0:
            print(f'Число {num} не является простым.')
            break
        elif i == num - 2:
            print(f'Число {num} - простое.')
            break