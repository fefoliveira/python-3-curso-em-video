"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

exp = str(input('Digite a expressão: '))
lista = []
cont = 0
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('Sua expressão é inválida.')
else:
    print('Sua expressão é válida.')
