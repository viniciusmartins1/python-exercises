print('========= LOJAS MARTINS =========')
compra = float(input('Preços das compras: '))
print(""""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    print('Sua compra de R$ {} vai custar R$ {}'.format(compra, compra - (compra * 0.1)))
elif opcao == 2:
    print('Sua compra de R$ {} vai custar R$ {}'.format(compra, compra - (compra * 0.05)))
elif opcao == 3:
    print('Sua compra de vai custar R$ {}'.format(compra))
elif opcao == 4:
    n = int(input('Quantas parcelas?'))
    juros = compra + compra * 0.2
    print('Sua compra será parcelada em {}x de R$ {} COM JUROS'.format(n, juros/ n ))
    print('Sua compra de R$ {} vai custar R$ {}'.format(compra, juros))
