'''
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии.
'''


def gen_vocab(name_list: list, rate_list: list, bonus_list: list) -> dict:
    bonus_gen = (float(it.replace('%', '')) for it in bonus_list)
    bonus_res_gen = (item[0] * item[1] /100 for item in zip(rate_list, bonus_gen))
    res_dict = {k: v for (k, v) in zip(name_list, bonus_res_gen)}
    print(res_dict)
    

if __name__ == '__main__':
    gen_vocab(['ivan', 'maria'], [100, 90], ['10.25%', '11.48%'])