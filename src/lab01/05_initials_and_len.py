a = input('Введи ФИО: ')
inn = [x for x in a.split() if len(x)>1]
b = [x for x in a if x!=' ']
print(f'ФИО: {a}')
print(f'Инициалы: {inn[0][0]+inn[1][0]+inn[2][0]}.')
print(f'Длина (символов): {len(b)}')
