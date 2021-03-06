j = 'S'
s = 0
c = 0
m = 0
menor = 0
while j == 'S':
    n = int(input('Digite um número: '))
    j = str(input('Quer continuar: [S/N] ')).upper()
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > m:
            m = n
        if n < menor:
            menor = n
print('Você digitou {} numeros e a média entre eles foi {:.2f}'.format(c, s/c))
print('O maior número digitado foi {} e o menor {} '.format(m, menor))



