from datetime import date
anoatual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = anoatual - ano
if idade == 18:
    print('Quem nasceu em {} tem {} anos'.format(ano, idade))
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    n = 18 - idade
    print('Quem nasceu em {} tem {} anos!'.format(ano, idade))
    print('Você aida falta {} para se alistar!'.format(n))
else:
    n = idade - 18
    print('Quem nasceu em {} tem {} anos!'.format(ano, idade))
    print('Você deveria ter se  alistado há {} anos!'.format(n))
    d = anoatual - n
    print('Seu alistamento foi em {}'.format(d))


