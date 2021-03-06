from time import sleep
from random import randint
print(''''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
computador = randint(0, 2)
print('=-' * 10)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('=-' * 10)
if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('Computador VENCE')
    elif computador == 2:
        print('Jogador VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif jogador == 1:
    if computador == 0:
        print('Jogador Vence')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('Computador VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif jogador == 2:
    if computador == 0:
        print('Computador VENCE!')
    elif computador == 1:
        print('Jogador VENCE!')
    elif computador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

