import random
ale = random.randint(0, 10)
print('Sou seu computador ...')
print('Acabei de pensar em um número entre 0 e 10!')
print('Será que voce consegue advinhar qual foi?')
n = 11
c = 0
while ale != n:
    n = int(input('Qual é o seu palpite? '))
    if ale > n:
        print('Mais .....Tente mais uma vez!')
    else:
        print('Menos.... Tente mais uma vez')
    c += 1
if n == ale:
    print('Parabéns!! Acertou com {} tentativas.'.format(c))

