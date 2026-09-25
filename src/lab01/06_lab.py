t = 0
f = 0
a = int(input('in_1: '))
for x in range(a):
    a2 = input(f'in_{x+2}: ').split()
    if len(a2) == 4:
        if a2[3] == 'True':
            t+=1
        else:
            f+=1
    else:
        print('Неверный ввод')
    
print(f'out: {t} {f}')
