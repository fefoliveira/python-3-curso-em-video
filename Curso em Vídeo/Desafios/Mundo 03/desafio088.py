"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
lista = list()
jogo = list()
qtd_jogos = int(input('Digite a quantia de jogos a serem realizados: '))
for i in range(0, qtd_jogos):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    lista.append(jogo[:])
    jogo.clear()
print(f'\nSegue a lista de jogos:')
for i in range(0, qtd_jogos):
    lista[i].sort()
    sleep(0.4)
    print(f'{i+1}º jogo: {lista[i]}')
