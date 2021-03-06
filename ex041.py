from datetime import date
anoatual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = anoatual - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO : Mirim!')
elif idade <= 14:
    print('CLASSIFICAÇÃO: Infantil!')
elif idade <= 19:
    print('CLASSIFICAÇÃO: Junior!')
elif idade <= 25:
    print('CLASSIFICAÇÃO: Sênior!')
elif idade > 25:
    print('CLASSIFICAÇÃO: Master!')

