from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
maior = n1
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar  
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('»»»» Qual a sua opção: '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} multiplicado por {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n2 > maior:
            maior = n2
        else:
            maior = n1
        print('O maior número foi {}'.format(maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção INVÁLIDA!!')
    print('-=' * 20)
sleep(1)
print('Fim do programa! Volte sempre!!')






