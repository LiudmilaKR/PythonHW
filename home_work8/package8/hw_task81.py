'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней 
с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle


def walk_dir(path_dir: str) -> dict:
    res_dict = {'name': os.path.basename(path_dir)}
    if os.path.isdir(path_dir):
        res_dict['type'] = 'directory'
        # res_dict['subdirectory'] = [walk_dir(os.path.join(path_dir, el)) for el in os.listdir(path_dir)]
        res_dict['content'] = []
        for el in os.listdir(path_dir):
            res_dict['content'].append(walk_dir(os.path.join(path_dir, el)))
    else:
        res_dict['type'] = 'file'
        res_dict['size'] = os.path.getsize(path_dir)
    return res_dict


def put_to_json(r_dict: dict):
    with open('hw_task81.json', 'w', encoding='utf-8') as f:
        json.dump(r_dict, f, indent=2)


def put_to_csv(r_dict: dict):
    with open('hw_task81.csv', 'w', newline='', encoding='utf-8') as f:
        # csv_writer = csv.DictWriter(f, dialect='excel', fieldnames=['name', 'type', 'content'])
        # csv_writer.writeheader()
        # csv_writer.writerow([r_dict])
        for k, v in r_dict.items():
            f.write(f'{k},{v}\n')


def put_to_pickle(r_dict: dict):
    with open('hw_task81.pickle', 'wb') as f:
        pickle.dump(r_dict, f)

if __name__ == '__main__':
    # print(os.getcwd())
    # os.chdir(os.pardir)
    # os.chdir('../..')
    # os.chdir('../')
    # print(os.getcwd())
    # put_to_json(os.getcwd())
    cur_dict = walk_dir('C:/Users/lidia/PythonProjects/Homeworks/home_work7')
    put_to_json(cur_dict)
    put_to_csv(cur_dict)
