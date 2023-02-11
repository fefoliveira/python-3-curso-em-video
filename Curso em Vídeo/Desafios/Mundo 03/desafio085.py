"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

lista = list()
pares = list()
impares = list()
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor inteiro: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
lista.append(pares[:])
lista.append(impares[:])
lista[0].sort()
lista[1].sort()
print(f'\nOs valores pares digitados foram: {lista[0]} '
      f'\nOs valores ímpares digitados foram: {lista[1]}')
