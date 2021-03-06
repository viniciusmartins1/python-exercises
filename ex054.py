from datetime import date
anoatual = date.today().year
tm = 0
tj = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    if anoatual - ano >= 18:
        tm += 1
    else:
        tj += 1
print('=' *45)
print('Ao todo tivemos {} pessoas maiores de idade!'.format(tm))
print('E também tivemos {} pessoas menores de idade!'.format(tj))
