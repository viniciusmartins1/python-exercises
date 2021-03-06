a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print(termo, end=' » ')
        termo += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar mais: '))
print('Progressao finalizada com {} termos mostrados'.format(tot))

