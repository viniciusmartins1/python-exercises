from time import sleep
print('\033[4;34m =- \033[m' * 15)
num = int(input('Digite umm número para ver a sua tabuada: '))
print('\033[4;34m =- \033[m' * 15)
for c in range(1, 11):
    print('\033[4m|{}| x |{}| = |{}|\033[m'.format(num, c, num * c))
    sleep(0.3)
print('\033[1;31mFIM!\033[m')

