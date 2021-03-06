nome = input('Digite seu nome completo: ')
print('Analisando seu nome....')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome.strip()) - nome.count(' ')))
nome2 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome2[0], len(nome2[0])))

