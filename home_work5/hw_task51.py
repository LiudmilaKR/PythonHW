'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''


def way_tuple(path_line: str) -> tuple:
    """_summary_ функция трансформации строкового пути до файла

    Args:
        path_line (str): _description_ абсолютный путь до файла

    Returns:
        tuple: _description_ кортеж из трёх элементов: путь, имя файла, расширение файла
    """
    # path_list = path_line.split('/')
    # return '/'.join(path_list[:-1]), path_list[-1].split('.')[0], path_list[-1].split('.')[1]
    path_f, *_, name_f = path_line.split('/')
    name_f, suf_f = name_f.split('.')
    return path_f, name_f, suf_f


if __name__ == '__main__':
    print(way_tuple('C:/Users/lidia/PythonProjects/Seminars/seminar7/example74/xlft.txt'))
    