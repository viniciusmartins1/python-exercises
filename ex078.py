num = list()
men = mai = 0
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        men = mai = num[cont]
    else:
        if num[cont] > mai:
            mai = num[cont]
        if num[cont] < men:
            men = num[cont]
print('=-='*15)
print(f'Você digitou os valores {num}')
print(f'O maior valor foi {mai} na posição ', end=' ')
for i, n in enumerate(num):
    if n == mai:
        print(i, end='... ')
print()
print(f'O menor valor foi {men} na posição ', end='')
for i, n in enumerate(num):
    if n == men:
        print(f'{i}...', end=' ')
print()
print('=-='*15)








