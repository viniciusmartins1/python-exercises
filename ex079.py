num = list()
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('valor cadastrado com sucesso!')
    else:
        print('Número duplicado! Não vou adicionar!')
    resp = input('Quer continuar? [S/N] ').upper()
    if resp in 'N':
        break
print('=-='*15)
num.sort()
print(f'Você digitou os números {num}')








