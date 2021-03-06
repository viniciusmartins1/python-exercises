num = int(input('Digite um número INTEIRO: '))
print("""Escolha uma da bases para conversão:
\033[0;36m[1] converte para BINÁRIO.\033[m
\033[0;35m[2] converte para OCTAL.\033[m
\033[0;33m[3] converte para HEXADECIMAL.\033[m """)
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO fica \033[0;36m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL fica \033[1;35m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL fica \033[1;33m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[0;31m OPÇÃO INVÁLIDA \033[m')

