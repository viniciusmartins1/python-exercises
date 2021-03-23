valores = list()
while True:
    num = int(input("Digite um número"))
    valores.append(num)
    cont = input("Quer continuar").upper()
    if cont == 'N':
        break
print(f"Você digitou {len(valores)} valores")
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
if 5 in valores:
    print("O valor 5 está na lista")
else:
    print('o valor 5 não está na lista')
