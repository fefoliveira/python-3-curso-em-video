"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre os três conteúdos das trÊs listas geradas."""

lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um número (0 para parar): '))
    if num == 0:
        break
    else:
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
if len(lista) == 0:
    print('\nNenhum número foi digitado.')
else:
    lista.sort()
    pares.sort()
    impares.sort()
    print(f'\nLista de todos os números digitados: {lista}')
    if len(pares) == 0:
        print('Nenhum número par foi digitado.')
    else:
        print(f'Lista de todos os números pares digitados: {pares}')
    if len(lista) == 0:
        print('Nenhum número ímpar foi digitado.')
    else:
        print(f'Lista de todos os números ímpares digitados: {impares}')
