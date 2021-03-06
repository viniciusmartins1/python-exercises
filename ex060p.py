num = int(input('Digite um número para ver seu fatorial: '))
f = 1
print('Cauculando {}! = '.format(f), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))


