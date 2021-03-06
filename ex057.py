sexo = input('Iforme seu sexo: [M/F] ').upper()[0].strip()
while sexo not in 'MF':
    sexo = input('Dados Inválidos! Digite o sexo novamente: ').upper()[0].strip()
print('Sexo {} cadastrado com sucesso!'.format(sexo))



