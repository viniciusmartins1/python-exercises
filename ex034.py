s = float(input('Qual o salário do funcionário? R$ '))
if s <= 1250:
    print('Quem ganhava R$ {:.2f} vai passar a ganhar R$ {:.2f}'.format(s, s * 1.15))
else:
    print('Quem ganhava R$ {:.2f} vai passar R$ {:.2f}'.format(s, s * 1.10))
