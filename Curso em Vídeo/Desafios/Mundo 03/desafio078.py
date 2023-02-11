"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista"""

maior = 0
menor = 0
pmaior = 0
pmenor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º número: ')))
    if valores[c] == 0:
        maior = valores[c]
        pmaior = c
        menor = valores[c]
        pmenor = c
    elif valores[c] > valores[c-1]:
        maior = valores[c]
        pmaior = c
    elif valores[c] < valores[c-1]:
        menor = valores[c]
        pmenor = c
print()
if maior == menor:
    print('Todos os valores são iguais.')
else:
    print(f'Você digitou os valores \033[35m{valores}\033[m.')
    print(f"O maior valor digitado foi \033[32m{maior}\033[m e se encontra na posição \033[33m{pmaior}\033[m da lista")
    print(f'O menor valor digitado foi \033[32m{menor}\033[m e se encontra na posição \033[33m{pmenor}\033[m da lista')
