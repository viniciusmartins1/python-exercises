casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print('Para pagar uma  casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}!'.format(casa, anos, prestacao))
    print('\033[4;31m Empréstimo NEGADO! \033[m')
else:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestacao será de R$ {:.2f}!'.format(casa, anos, prestacao))
    print('\033[4;33m Empréstimo feito com SUCESSO \033[m')


