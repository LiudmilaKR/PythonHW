import json
import os
import pickle


def read_json():
    """_summary_ функция считывает словарь

    Returns: словарь
        _type_: _description_
    """
    if os.path.exists('result82.json'):
        with open('result82.json', 'r', encoding='utf-8') as jf:
            access_dict = json.load(jf)
    else:
        access_dict = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {},}
    print(access_dict)
    return access_dict


def write_to_json(access_dict: dict):
    """_summary_ функция бесконечном цикле запрашивает имя, личный идентификатор 
    и уровень доступа (от 1 до 7), записывает данные в файл json и csv

    Args:
        access_dict (dict): _description_
    """
    while True:
        name = input('Введите имя => ')
        
        while True:
            flag = False
            ident = input('Введите ID => ')
    # необходимо убедится, что ID уникальный
            for k, v in access_dict.items():
                if ident in v.keys():
                    print('Такой ID уже есть!')
                    flag = True
            if not flag:
                break
        
        while True:
            access_level = input('Введите уровень доступа => ')
            if '0' < access_level < '8':
                break
        
        access_dict[access_level][ident] = name
        
        s = input('Закончили? y/n => ')
        if s == 'y':
            break
    
    with open('result82.json', 'w', encoding='utf-8') as f:
        json.dump(access_dict, f, indent=4, ensure_ascii=False)
    print('Final json')
    
    with open('result82.csv', 'w', encoding='utf-8') as csf_f:
        for key, value in access_dict.items():
            for k, v in value.items():
                csf_f.write(f'{key},{k},{v}\n')


def csv_to_json(csv_name: str, json_name: str):
    """_summary_ функция читает csv файл без использования csv.DictReader, 
    дополняет id до 10 цифр незначащими нулями, в именах первую букву делает прописной.
    Получившиеся записи сохраняется в json файл.

    Args:
        csv_name (str): _description_
        json_name (str): _description_

    Raises:
        FileNotFoundError: _description_
    """
    if not os.path.exists(csv_name):
        raise FileNotFoundError('нет файла')
    
    with (
        open(csv_name, 'r', encoding='utf-8') as cf,
        open(json_name, 'a', encoding='utf-8') as jf
        ):
        for line in cf:
            level, ident, name = line.strip().split(',')
            ident = f'{int(ident):010d}'
            name = name.title()
            hash_name = hash(name + ident)
            my_dict = {level: [ident, name, hash_name]}
            # jf.write(json.dumps(my_dict))
            print(json.dumps(my_dict), file=jf)


class NotDirError(Exception):
    def __str__(self):
        return 'директория не существует'


def json_to_pickle(dir_name: str):
    """_summary_ функция ищет json файлы в указанной директории и 
сохраняет их содержимое в виде одноимённых pickle файлов

    Args:
        dir_name (str): _description_

    Raises:
        NotDirError: _description_
    """
    if not os.path.exists(dir_name) or not os.path.isdir(dir_name):
        raise NotDirError
    # not os.path.isdir(dir_name) - если не директория
    for file_name in os.listdir(dir_name):
        if file_name.endswith('81.json'):
            with (
                # open(os.path.join(dir_name, file_name), 'r', encoding='unf-8') as jf,
                open(os.path.join(dir_name, file_name), 'r') as jf,
                open(os.path.join(dir_name, file_name.replace('.json', '.pickle')), 'wb') as pf
                  ):
                data = json.load(jf)
                pickle.dump(data, pf)
