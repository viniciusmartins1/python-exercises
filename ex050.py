s = 0
tp = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        tp += 1
print('Você informou {} números PARES e a soma deles é {}'.format(tp, s))

