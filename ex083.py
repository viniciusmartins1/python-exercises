valores = list()
expressao = str(input('Digite a expressão: '))
pareFechando = 0
pareAbrindo = 0
for simb in expressao:
    if simb == '(':
        valores.append('(')
    elif simb == ')':
        if len(valores) > 0:
            valores.pop()
        else:
            valores.append(')')
            break

if len(valores) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')
