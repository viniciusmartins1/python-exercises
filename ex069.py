print('=' * 30)
print('{^} CADASTRE UMA PESSOA')
print('=' * 30)
totidade = 0
tothome = 0
totmul = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    print('-' * 20)
    if idade >= 18:
        totidade += 1
    if sexo == 'M':
        tothome += 1
    if sexo == 'F' and idade < 20:
        totmul += 1
    c = input('Quer continuar? [S/N] ').upper()
    if c == 'N':
        print('-' * 20)
        break
print(f'Total de pessoas com 18 anos: {totidade}!')
print(f'Ao todo temos {tothome} homens cadastrados!')
print(f'E temos {totmul} mulheres com menos de 20 anos!')




