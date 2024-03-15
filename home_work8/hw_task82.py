'''
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''

from package8 import walk_dir, put_to_json, put_to_csv, put_to_pickle

import os


cur_dir = walk_dir(os.getcwd())
put_to_json(cur_dir)
put_to_csv(cur_dir)
put_to_pickle(cur_dir)
