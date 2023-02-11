"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

from time import sleep
print('Veja todos os números pares que estão no intervalo entre 1 e 50:')
sleep(1)
for c in range(2, 51, 2):
    print(c, end='; ')
print('\033[31mFIM\033[m.')
