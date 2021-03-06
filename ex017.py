import math
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(cata, cato)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
