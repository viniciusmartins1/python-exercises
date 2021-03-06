na = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',)
nb = ('nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesséis', 'dezessete')
nc = ('dezoito', 'dezenove', 'vinte')
n = na + nb + nc
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    else:
        print(f'Você digitou o número {n[num]}')
        break
        
