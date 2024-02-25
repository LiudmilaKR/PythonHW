'''
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''


def main():
    """_summary_ функция основного меню
    """
    global glob_list
    balance, count = 0, 0
    print('Добрро пожаловать в Банкомат.')
    while True:
        while True:
            act = input('Выберите действие:\n1 - пополнить\n2 - снять\n3 - выйти\n')
            if act not in ['1', '2', '3']:
                print('Некорректный ввод.')
            else:
                break
        
        match act:
            case '1':
                balance, count = add_money(balance, count)
                print(f'Ваш баланс {balance:0.2f} рублей.')
            case '2':
                balance, count = get_money(balance, count)
                print(f'Ваш баланс {balance:0.2f} рублей.')
            case '3':
                print(f'Ваши операции => {glob_list}\nВаш баланс {balance:0.2f} рублей.\nДо свидания!')
                break

def add_money(balance:int, count:int) -> int:
    """_summary_ функция пополнения счета

    Args:
        balance (int): _description_ баланс счета
        count (int): _description_ счетчик операций

    Returns:
        int: _description_ баланс и счетчик
    """
    global glob_list
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input('Введите сумму пополнения, кратную 50 руб => '))
        except:
            ex = input('Хотите выйти в меню? ')
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    glob_list.append(summ)
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count

def get_money(balance: int, count: int) -> int:
    """_summary_ функция снятия денег со счета

    Args:
        balance (int): _description_ баланс счета
        count (int): _description_ счетчик операций

    Returns:
        int: _description_ баланс и счетчик
    """
    global glob_list
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input('Введите сумму снятия, кратную 50 руб => '))
        except:
            ex = input('Хотите выйти в меню? ')
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if (summ + perc) > balance:
                print('')
                continue
            else:
                break
    balance -= (summ + perc)
    glob_list.append(-summ)
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count

if __name__ == "__main__":
    glob_list = []
    main()