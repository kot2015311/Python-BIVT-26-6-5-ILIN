t = 0
f = 0
a = int(input('in_1: '))
for x in range(a):
    a2 = input(f'in_{x+2}: ').split()
    if a2[3] == 'True':
        t+=1
    else:
        f+=1
print(f'out: {t} {f}')
