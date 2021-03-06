l = float(input('Largura da Parede: '))
a = float(input('Altura da Parede: '))
area = l * a
print('Sua parede tem dimensão {} x {} e possui uma área de {} '.format(l, a, area))
print('Para pintar essa parede, você precisará de {} m2'.format(area / 2))

