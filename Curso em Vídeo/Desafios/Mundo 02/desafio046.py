"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep
from emoji import emojize
print('Contagem regressiva para a queima de fogos!')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[33mFeliz ano novo! {}\033[m'.format(emojize(':fireworks:')))
