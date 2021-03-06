from random import randint
s = 0
tot = 0
print('-='*30)
print('Vamos jogar PAR ou ÍMPAR')
print('-='*30)
while True:
    jogador = int(input('Digite um valor: '))
    pi = input('Par ou Impar: [P/I] ').upper()
    print('-'*20)
    computador = randint(1, 10)
    s = jogador + computador
    print('=-'*20)
    print(f'Voce jogou {jogador} e o computador {computador}. ', end='')
    print('=-'*20)
    if s % 2 == 0:
        print(f'O total {s} DEU PAR')
        if pi == 'P':
            print('Voce VENCEU!!')
            tot += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'O total {s} DEU IMPAR!')
        if pi == 'I':
            print('Você VENCEU!!')
            tot += 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente!')
        print('-=' * 20)
print(f'GAME OVER!! Você ganhou {tot} vezes')



