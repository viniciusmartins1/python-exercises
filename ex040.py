n1 = float(input('Primeiora nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {} a média do aluno é {}'.format(n1, n2, media))
if media < 5:
    print('O aluno está \033[4;31m REPROVADO \033[m')
elif media >= 5 and media <= 6.9:
    print('O aluno está em \033[4;33m RECUPERAÇÃO \033[4;33m')
else:
    print('O aluno está \033[4;32m APROVADO \033[4;32m')

