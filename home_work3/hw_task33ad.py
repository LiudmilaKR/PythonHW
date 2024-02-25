from itertools import permutations

MAX_WEIGHT = 3

# belongings_list = {'рюкзак': 1.5, 'фонарик': 0.15, 'спальник': 2.61, 'коврик': 0.53, 'вода': 0.45}
belongings_list = {'рюкзак': 1.5, 'фонарик': 0.15, 'спальник': 2.8, 'коврик': 0.53, 
                   'посуда': 0.35, 'купальник': 0.2, 'вода': 0.45, 'компас': 0.1, 'аптечка': 0.47}

# вариант 1
# cur_weight1 = 0
# res_list1 = dict()
# for k, v in belongings_list.items():
#     if cur_weight1 + v < MAX_WEIGHT:
#         res_list1.update({k: v})
#         cur_weight1 += v
# print(res_list1)

# вариант 2
# cur_list2 = []
# res_list2 = dict()
# for k, v in belongings_list.items():
#     cur_list2.append(v)
#     if sum(cur_list2) < MAX_WEIGHT:
#         res_list2.update({k: v})
#     else:
#         cur_list2.pop()
# print(res_list2)

# вариант 3
cur_list3 = []
res_list3 = []
res_set = set()
for perm in permutations(belongings_list.items()):
    for i in range(len(perm)):
        cur_list3.append(perm[i][1])
        if sum(cur_list3) < MAX_WEIGHT:
            res_list3.append(perm[i][0])
        else:
            cur_list3.pop()
    res_set.add(frozenset(res_list3))
    cur_list3.clear()
    res_list3.clear()
for item in res_set:
    print(item)
    