"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint
r1 = randint(0, 10)
r2 = randint(0, 10)
r3 = randint(0, 10)
r4 = randint(0, 10)
r5 = randint(0, 10)
tupla = (r1, r2, r3, r4, r5)
print(f'Os valores sorteados foram: {tupla}')

maior = tupla[0]
menor = tupla[0]
for cont in range(len(tupla)):
    if tupla[cont] > maior:
        maior = tupla[cont]
    elif tupla[cont] < menor:
        menor = tupla[cont]
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
