'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
'''

my_str = 'List, список является самой часто используемой коллекцией в Python. Прежде чем говорить о списках, я напомню, \
    что такое массив в информатике. Массив - это непрерывная область в оперативной памяти компьютера, поделённая на ячейки \
    что такое массив в информатике. Массив - это непрерывная область в оперативной памяти компьютера, поделённая на ячейки \
    одинакового размера хранящие данные одного типа. Массивы могут быть статическими, то есть размер массива нельзя изменить, \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
        и динамическими, когда размер массива изменяется при добавлении или удалении элементов. Один из самых больших плюсов \
            в работе с массивами — это доступ к любой из его ячеек за константное время. Массив — упорядоченный набор элементов, \
                каждый из которых хранит одно значение, идентифицируемое с помощью одного или нескольких индексов. В простейшем \
                    случае массив имеет постоянную длину и хранит единицы данных одного и того же типа, а в качестве индексов \
                    случае массив имеет постоянную длину и хранит единицы данных одного и того же типа, а в качестве индексов \
                    случае массив имеет постоянную длину и хранит единицы данных одного и того же типа, а в качестве индексов \
                    случае массив имеет постоянную длину и хранит единицы данных одного и того же типа, а в качестве индексов \
                    случае массив имеет постоянную длину и хранит единицы данных одного и того же типа, а в качестве индексов \
                        выступают целые числа. В информатике, список (англ. list) — это абстрактный тип данных, представляющий \
собой упорядоченный набор значений, в котором некоторое значение может встречаться более одного раза. Экземпляр списка является \
    компьютерной реализацией математического понятия конечной последовательности. Экземпляры значений, находящихся в списке, \
    компьютерной реализацией математического понятия конечной последовательности. Экземпляры значений, находящихся в списке, \
    компьютерной реализацией математического понятия конечной последовательности. Экземпляры значений, находящихся в списке, \
        называются элементами списка (англ. item, entry либо element); если значение встречается несколько раз, каждое \
            вхождениесчитается отдельным элементом. доступ доступ доступ, данные данные данные данные данные данные, асбстрактные \
                асбстрактные асбстрактные асбстрактные асбстрактные асбстрактные асбстрактные асбстрактные асбстрактные. каждый \
                    каждый каждый. python python python python python python python python python python python python python.'
for c in my_str:
    if c in ('.', ',', '-', '!', '(', ')'):
        my_str = my_str.replace(c, '')
my_list = my_str.lower().split()
my_dict = {}
for item in my_list:
    if item not in my_dict:
        my_dict[item] = 1
    else:
        my_dict[item] += 1
v_set = set(list(set(my_dict.values()))[:-11:-1])
for k, v in my_dict.items():
    if v in v_set:
        print(f'слово "{k}" встречается {v} раз')
        