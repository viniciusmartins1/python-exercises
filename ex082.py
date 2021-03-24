lista = list()
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
pares = list()
impa = list()
for valor in range(len(lista)):
    if lista[valor] % 2 == 0:
        pares.append(lista[valor])
    else:
        impa.append(lista[valor])
print('-=-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impa}')

