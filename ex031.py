d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print('Você esta prestes a começar um viagem de {} km'.format(d))
    print('A sua viaggem vai custar R$ {:.2f}'.format(d * 0.5))
else:
    print('Você esta prestes a comecar um viage de {} km'.format(d))
    print('A sua viagem vai custar R$ {:.2f}'.format(d * 0.45))
