'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

from datetime import datetime
from calendar import isleap
from sys import argv


def check_date(date: str) -> bool:
    format = '%d.%m.%Y'
    try:
        date = datetime.strptime(date, format)
        # print(date)
        return True
    except:
        return False


def check_year(year: int) -> bool:
    return isleap(year)


if __name__ == '__main__':
    # из текущей папки вводим команду: python hw_task61.py 25.02.2005 2024
    if check_date(argv[1]):
        print('Дата существует.')
    else:
        print('Дата не сущестует.')
    
    if check_year(int(argv[2])):
        print('Год високосный.')
    else:
        print('Год не високосный.')    
    