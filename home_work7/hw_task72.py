'''
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''

from package7 import gen_file_to_directory, rename_files

files_dir = 'hw7/'
gen_file_to_directory('.png', files_dir, num_files=3)
gen_file_to_directory('.txt', files_dir, num_files=5)
gen_file_to_directory('.mkd', files_dir, num_files=3)
rename_files('file', 5, 'mkd', 'txt', [2, 5], files_dir)
