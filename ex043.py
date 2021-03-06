peso = float(input('Qual o seu peso? (kg) '))
altu = float(input('Qual a sua altura? (m) '))
imc = peso/ (altu ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO' )
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS! Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Você está SOBREPESO')
elif imc >= 30 and imc <= 40:
    print('Cuidado! OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')


