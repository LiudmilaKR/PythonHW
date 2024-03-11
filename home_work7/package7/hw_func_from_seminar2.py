from random import randint
import os


def gen_file_name(num_char: int) -> str:
    """_summary_ генерация имени файла

    Args:
        num_char (int): _description_количество символов в имени

    Returns:
        str: _description_ имя файла
    """
    list_name = []
    for i in range(num_char):
        list_name.append(chr(randint(ord('a'), ord('z'))))
    return ''.join(list_name)


def gen_file(extent: str, min_len: int = 6, max_len: int = 30, 
             min_bites: int = 256, max_bites: int = 4096, 
             num_files: int = 3):
    """_summary_ генерация файлов
    
    Args:
        extent (str): _description_ расширение файлов
        min_len (int, optional): _description_. Defaults to 6 - минимальная длина имени файла
        max_len (int, optional): _description_. Defaults to 30 - максимальная длина имени файлов
        min_bites (int, optional): _description_. Defaults to 256 - минимальное количество байтов в файле
        max_bites (int, optional): _description_. Defaults to 4096 - максимальное количество байтов в файле
        num_files (int, optional): _description_. Defaults to 3 - количество генерируемых файлов
    """
    for i in range(num_files):
        name = gen_file_name(randint(min_len, max_len))
        bytes = gen_file_name(randint(min_bites, max_bites))
        with open('Seminars/seminar7/example74/' + name + extent, 'a', encoding='UTF-8') as f:
            f.write(bytes)


def get_dict(ext: dict):
    """_summary_ генерация файлов с разными расширениями
    
    Args:
        ext (dict): _description_ словарь: ключ - расширение, значение - количество файлов
    """
    for k, v in ext.items():
        gen_file(extent=k, num_files=v)


def gen_file_to_directory(exten: str, directory: str, min_len: int = 6, max_len: int = 30, 
             min_bites: int = 256, max_bites: int = 4096, 
             num_files: int = 3):
    """_summary_ генерация файлов в указанную директорию

    Args:
        exten (str): _description_ расширение файлов
        directory (str): _description_ директория
        min_len (int, optional): _description_. Defaults to 6 - минимальная длина имени файла
        max_len (int, optional): _description_. Defaults to 30 - максимальная длина имени файлов
        min_bites (int, optional): _description_. Defaults to 256 - минимальное количество байтов в файле
        max_bites (int, optional): _description_. Defaults to 4096 - максимальное количество байтов в файле
        num_files (int, optional): _description_. Defaults to 3 - количество генерируемых файлов
    """
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    
    for i in range(num_files):
        while True:
            name = gen_file_name(randint(min_len, max_len))
            if name + exten not in os.listdir(directory):
                break
        bytes = gen_file_name(randint(min_bites, max_bites))
        with open(directory + name + exten, 'a', encoding='UTF-8') as f:
            f.write(bytes)



def sort_file(directory: str = 'Seminars/seminar7/example74/'):
    """_summary_ сортировка файлов по директориям

    Args:
        directory (str, optional): _description_. Defaults to 'Seminars/seminar7/example74/'.
    """
    my_dict = {'jpeg': 'foto', 'png': 'foto', 'mrk': 'text', 'txt': 'text'}
    for file in os.listdir(directory):
        file_exten = file.split('.')[-1]
        if file_exten in my_dict.keys():
            if not os.path.exists('Seminars/seminar7/' + my_dict[file_exten]) \
            or not os.path.isdir('Seminars/seminar7/' + my_dict[file_exten]):
                os.mkdir('Seminars/seminar7/' + my_dict[file_exten])
            os.rename(os.path.join(directory, file), os.path.join('Seminars/seminar7/' + my_dict[file_exten], file))


if __name__ == '__main__':
    gen_file_to_directory('txt', 'hw7/')
