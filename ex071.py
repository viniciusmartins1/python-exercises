print('='* 30)
print('{:^30}'.format('Simulador de Banco'))
print('='* 30)
dinheiro = int(input('Quanto você quer sacar? R$ '))
total = dinheiro
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${ced}!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break



