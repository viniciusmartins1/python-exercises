s = 0
i = 0
for c in range(1, 501,):
    if c % 2 == 1 and c % 3 == 0:
        i += 1
        s += c
print('A soma de todos os {} solicitados é {}'.format(i, s))


