kt = 0 # Не совсем понял условие. Откуда должны приходить данные о людях, заранее или после ввода числа? Поэтому закинул в цикл.
kf = 0
data = []
n = int(input("Число для регистрации: ")) 
for x in range(n):
    a = input('Введи ФИО и возраст: ')
    b = input("Формат обучения: ")
    if b == 'Очно': b = True; kt +=1
    else: b = False; kf +=1
    i = a+str(b)
    data.append(i)
print(f"Количество участников: {n}")
for x in data:
    print(x)
print(f'out: {kt} {kf}')