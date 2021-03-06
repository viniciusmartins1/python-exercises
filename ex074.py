from random import randint
num = (randint(1,10), randint(1,10), randint(1,10),
        randint(1,10), randint(1,10))
for n in num:
    print(n, end=' ')
print(f'\nO maior número sorteado foi {max(num)}',)
print(f'O menor número sorteado foi {min(num)}')



