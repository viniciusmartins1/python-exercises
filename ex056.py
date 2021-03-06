s = 0
maior = 0
hm = 0
nm = ''
tot = 0
for c in range(1, 5):
    print('------ {} ------'.format(c))
    n = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo : [M/F] ').upper()
    s += idade
    if sexo == 'F' and idade < 20:
        tot += 1
    if idade > maior:
        maior = idade
        if sexo == 'M':
           hm = maior
           nm = n
print('A média da idade do grupo é de {}'.format(s/4))
print('O homem mais velho tem {} e se chama {}'.format(maior, nm))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot))





