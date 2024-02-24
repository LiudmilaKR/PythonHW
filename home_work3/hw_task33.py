'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
* Верните все возможные варианты комплектации рюкзака.
'''

from itertools import permutations

MAX_WEIGHT = 3

belongings_list = {'рюкзак': 1.5, 'фонарик': 0.15, 'спальник': 2.8, 'коврик': 0.53, 
                   'посуда': 0.35, 'купальник': 0.2, 'вода': 0.45, 'компас': 0.1, 'аптечка': 0.47}

# вариант 1
cur_weight = 0
cur_list = dict()
for k, v in belongings_list.items():
    if cur_weight + v < MAX_WEIGHT:
        cur_list.update({k: v})
        cur_weight += v
print(cur_list)

# вариант 2
# c_weight = 0
# c_list = []
# for perm in permutations(belongings_list.values()):
#     for i in perm:
#         if c_weight + i < MAX_WEIGHT:
#             c_list.append(i)
#             c_weight += i
#     print(c_list)
#     c_list.clear()
#     c_weight = 0
    