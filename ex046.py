from time import sleep
print('\033[4;32m =- \033[m' * 6)
print(' CONTAGEM REGRESSIVA')
print('\033[4;32m =- \033[m' * 6)
sleep(2)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1;31mBUM! BUM! POOW! \033[m')
