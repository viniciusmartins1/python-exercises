vel = float(input('Qual é a velocidade do carro? km  '))
if vel <= 80:
    print('Tem um bom dia! Dirija com segurança!!')
else:
    n = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R$ {}'.format(n))
    print('Tenha um bom dia! Dirija com segurança!')
