s = totp = menor = cont =  0
nome = ''
while True:
    produto = input('Nome do Produto: ')
    preco = int(input('Preço: '))
    print('-' * 20)
    s += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = produto
    if preco >= 1000:
        totp += 1
    c = input('Quer continuar ? [S/N] ').upper()
    while c not in 'SsNn':
        c = input('Quer continuar ? [S/N] ').upper()
    if c == 'N':
        break
print('... Finalizando compra ...')
print('-' * 20)
print(f'O total de compras foi {s}')
print(f'Temos {totp} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {nome} custando {menor}')


