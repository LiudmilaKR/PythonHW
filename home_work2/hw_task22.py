'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
'''

import fractions

line1 = input('Введите первую строку вида a/b => ')
line2 = input('Введите вторую строку вида a/b => ')

l11, l12 = line1.split('/')
l11, l12 = int(l11), int(l12)
fraction1 = fractions.Fraction(l11, l12)

l21, l22 = line2.split('/')
l21, l22 = int(l21), int(l22)
fraction2 = fractions.Fraction(l21, l22)

sum_numerator = l11 * l22 + l21 * l12
sum_denominator = l12 * l22

i = 2
while i <= min(sum_numerator, sum_denominator):
    if sum_numerator % i == 0 and sum_denominator % i == 0:
        sum_numerator /= i
        sum_denominator /= i
    else:
        i += 1
        
if sum_denominator == 1:
    sum = int(sum_numerator)
else:
    sum = str(int(sum_numerator)) + '/' + str(int(sum_denominator))
    
mult_numerator = l11 * l21
mult_denominator = l12 * l22

j = 2
while j <= min(mult_numerator, mult_denominator):
    if mult_numerator % j == 0 and mult_denominator % j == 0:
        mult_numerator /= j
        mult_denominator /= j
    else:
        j += 1
        
if mult_denominator == 1:
    mult = int(mult_numerator)
else:
    mult = str(int(mult_numerator)) + '/' + str(int(mult_denominator))

print(f'{line1} + {line2} = {sum}\n{line1} * {line2} = {mult}')

print('Check:')
print(f'{line1} + {line2} = {fraction1 + fraction2}\n{line1} * {line2} = {fraction1 * fraction2}')