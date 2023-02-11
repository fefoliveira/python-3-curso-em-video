"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
    A)Quantas pessoas foram cadastradas;
    B)Uma listagem com as pessoas mais pesadas;
    C)Uma listagem com as pessoas mais leves."""

lista = list()
aux = list()
pesadas = list()
leves = list()
cont = cont2 = mais_pes = mais_leve = 0
while True:
    cont += 1
    nome = str(input(f'{cont}º nome: '))
    aux.append(nome.capitalize())
    aux.append(float(input(f'{cont}º peso: ')))
    lista.append(aux[:])
    aux.clear()
    continua = str(input('Deseja continuar? [S/N]: '))
    while continua not in 'NnSs':
        continua = str(input('Inválido! Digite novamente se seseja continuar [S/N]: '))
    if continua in 'Nn':
        print()
        break
    print()
for p in lista:
    if cont2 == 0:
        mais_pes = mais_leve = p[1]
        cont2 = 1
    if p[1] > mais_pes:
        mais_pes = p[1]
    elif p[1] < mais_leve:
        mais_leve = p[1]
for p in lista:
    if p[1] == mais_pes:
        pesadas.append(p[0])
    elif p[1] == mais_leve:
        leves.append(p[0])
print(f'Foram cadastradas {cont} pessoas.')
if mais_pes == mais_leve:
    print(f'Todas as pessoas cadastradas tem o mesmo peso: {mais_pes}Kg.')
else:
    print(f'\nLista das pessoas mais pesadas (o maior peso foi de {mais_pes:.1f}Kg): {pesadas}'
          f'\nLista das pessoas mais leves (o menor peso foi de {mais_leve:.1f}Kg): {leves}')
