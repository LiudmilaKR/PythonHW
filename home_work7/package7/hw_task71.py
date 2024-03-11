'''
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
import os
import shutil

def rename_files(name: str, number_figures: int, ext_start: str, ext_finish: str, letters: list, directory: str):
    file_list = os.listdir(directory)
    # print(file_list)
    number = int(''.join(['1' for _ in range(number_figures)]))
    for i, obj in enumerate(file_list, number):
        if obj.split('.')[1] == ext_start:
            os.rename(os.path.join(directory, obj), 
                  os.path.join(directory, obj.split('.')[0][letters[0]:letters[1] + 1] + name + str(i) + '.' + ext_finish))


if __name__ == '__main__':
    rename_files('file', 3, 'bin', 'txt', [2, 5], 'C:/Users/lidia/PythonProjects/Homeworks/home_work7/hw7')
