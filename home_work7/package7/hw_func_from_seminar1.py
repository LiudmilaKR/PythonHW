from random import randint, random, choice
from typing import TextIO

VOWELS = {'a', 'o', 'u', 'e', 'i', 'y'}

def gen_nums(lines: int, name: str) -> None:
    """_summary_
функция, которая заполняет файл (добавляет в конец) случайными парами чисел.
    Args:
        lines (int): _description_ количество строк
        name (str): _description_ имя файла
    """
    with open(name, 'a', encoding='UTF-8') as f:
        for _ in range(lines):
            num1 = randint(-1000, 1000)
            num2 = random() * 2000 - 1000
            print(f'{num1} | {num2}', file=f)


def gen_name() -> str:
    """_summary_ Генерирует случайное имя. Имя должно начинаться с заглавной буквы, 
    состоять из 4-7 букв, среди которых обязательно должны быть гласные.
    Returns:
        str: _description_ имя
    """
    lens = randint(4, 7)
    min_letter = ord('a')
    max_letter = ord('z')
    
    name_list = []
    for _ in range(lens):
        name_list.append(chr(randint(min_letter, max_letter)))
    
    flag = False
    for l in name_list:
        if l in VOWELS:
            flag = True
            break

    if not flag:
        ind = randint(0, lens - 1)
        letter = choice(list(VOWELS))
        name_list[ind] = letter
    
    name = ''.join(name_list).capitalize()
    return name


def rec_file(lines: int, name: str):
    """_summary_ Записывает имена в файл

    Args:
        lines (int): _description_ кол-во имен
        name (str): _description_ имя файла
    """
    with open(name, 'a', encoding='UTF-8') as f:
        for _ in range(lines):
            f.write(f'{gen_name()}\n')


def read_line_or_begin(fd: TextIO) -> str:
    """_summary_ 
читаем файл, если файл закончился - читаем сначала
    Args:
        fd (TextIO): _description_ файл

    Returns:
        str: _description_ считываемый текст
    """
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def read_file(file1: str, file2: str, file3: str):
    """_summary_

    Args:
        file1 (str): _description_ файл с числами
        file2 (str): _description_ файл с именами
        file3 (str): _description_ файл, в который записывается обработанная инфо
    """
    with (open (file1, 'r', encoding='UTF-8') as f1, 
        open (file2, 'r', encoding='UTF-8') as f2, 
            open (file3, 'a', encoding='UTF-8') as f3):
        
        len1 = len(f1.readlines())
        len2 = len(f2.readlines())
        len3 = max(len1, len2)
        
        for _ in range(len3):
            line1 = read_line_or_begin(f1)
            name_f = read_line_or_begin(f2)
            a, b = [float(i) for i in line1.split(' | ')]
            res = a * b
            if res > 0:
                name_f = name_f.upper()
                res = round(res)
            else:
                name_f = name_f.lower()
                res = abs(res)
            
            f3.write(f'{name_f}: {res}\n')
