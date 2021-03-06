import random
from time import sleep
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
n = int(input('Em que número pensei? '))
ale = random.randint(0, 5)
print('Processando...')
sleep(1)
if n == ale:
    print('Parabéns!! Você conseguiu me vencer.')
else:
    print('Eu ganhei!! Tente novamente')


