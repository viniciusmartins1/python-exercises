print('='* 10)
print('10 TERMOS DE UM PA')
print('='* 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = a1 + (10 - 1) * r
for c in range(a1, d + r, r):
    print(c, end=' -> ')
print('ACABOU!')


