from time import sleep
for c in range(1, 51):
    if c % 2 == 0:
        sleep(0.3)
        print(c, end=' ')
print('Acabou....')
