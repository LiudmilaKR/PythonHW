'''
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''


def qeens_task(qeens: set) -> tuple:
    """_summary_ функция, проверяющая бьют ли ферзи друг друга

    Args:
        n (int): _description_ количество ферзей на доске 8x8

    Returns:
        tuple: _description_ False\True, ферзь, бьющий другие
    """

    
    for item in qeens:
        temp_list = list(qeens)
        temp_list.remove(item)
        if item[0] in [i[0] for i in qeens if i != item]:
            return True, item, set(temp_list)
        elif item[1] in [i[1] for i in qeens if i != item]:
            return True, item, set(temp_list)
        else:
            for it in temp_list:
                if (item[0] + item[1]) <= 9:
                    if it in [(i, j) for i, j in zip(range(item[0] + item[1] - 1, 0, -1), range(1, item[0] + item[1]))]:
                        return True, item, set(temp_list)
                else:
                    if it in [(i, j) for i, j in zip(range(8, item[0] + item[1] - 8 + 1, -1), range(item[0] + item[1] - 8, 8))]:
                        return True, item, set(temp_list)
                if item[0] <= item[1]:
                    if it in [(i, j) for i, j in zip(range(1, 8 - item[1] + item[0] + 1), range(item[1] - item[0] + 1, 9))]:
                        return True, item, set(temp_list)
                else:
                    if it in [(i, j) for i, j in zip(range(item[0] - item[1] + 1, 9), range(1, 8 - item[0] + item[1] + 1))]:
                        return True, item, set(temp_list)

        qeens = set(temp_list)
        if len(qeens) == 1:
            return False, item, set(temp_list)

if __name__ == '__main__':
    q = {(4, 4), (6, 7), (3, 8), (1, 2), (5, 6), (7, 5), (2, 5)}
    print(f'Текущая расстановка ферзей => {q}')
    res_tuple = qeens_task(q)
    if res_tuple[0]:
        print(f'Ферзь {res_tuple[1]} бъёт один из ферзей {res_tuple[2]}')
    else:
        print('Ни один из ферзей не бъет другие ферзи!')
    