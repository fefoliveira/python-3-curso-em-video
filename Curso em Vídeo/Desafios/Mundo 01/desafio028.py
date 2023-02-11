"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep
n = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)  # Estético
print('Vou penar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)  # Estético
j = int(input('Em que número eu pensei? ')) # O Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2) # Faz o programa dormir no tempo determinado
if j == n:
    print('Parabéns, você acertou! O número escolhido era {}.'.format(n))
else:
    print('Infelizmente você errou! O número escolhido era {}.'.format(n))
