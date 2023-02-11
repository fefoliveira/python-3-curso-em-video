"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:
    num = int(input('Digite um número (0 para parar): '))
    if num == 0:
        break
    else:
        lista.append(num)
if len(lista) == 0:
    print('\nNenhum número foi digitado.')
else:
    if len(lista) == 1:
        print('\nFoi digitado 1 número.')
    else:
        print(f'\nForam digitados {len(lista)} números.')
    lista.sort()
    print(f'A lista digitada é igual a: {lista}')
    if 5 in lista:
        print('O número 5 \033[32mESTÁ PRESENTE\033[m na lista.')
    else:
        print('O número 5 \033[31mNÃO\033[m está presente na lista.')

