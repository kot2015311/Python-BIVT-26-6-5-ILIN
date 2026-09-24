a = 'thisisabracadabraHt1eadljjl12ojh.'
print(f'in: {a}')
b = ''
for x in range(len(a)):
    if a[x] in 'QWERTYUIOPASDFGHJKLZXCVBNM': 
        k = a[x]
        
        b = b.join(k)
        d = a.index(k)
        break
for x in range(len(a)):
    if a[x] in '0123456789': 
        b += b.join(a[x+1])
        c = a.index(a[x+1])
        break
r = c-d 

for x in range(23,len(a),r):
    b += b.join(a[x])
print(f'out: {b}')