'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
используйте его строковое представление.
'''


def build_dict(**kwargs):
    # {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}
    return kwargs


if __name__ == '__main__':
    print(build_dict(a = 2, c = 'second', день = [1, 3, 7]))
