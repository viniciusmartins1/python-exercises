frase = input('Digite uma frase: ').upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for l in range(len(junto)-1, -1, -1):
    inverso += junto[l]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
