"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque em ordem, sabendo que o vencedor
tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador_1': randint(1, 6),
        'Jogador_2': randint(1, 6),
        'Jogador_3': randint(1, 6),
        'Jogador_4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.4)
rank = list()
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# itemgetter ordena por ordem de chave quando (0) e de valor quando (1)
print()
for i, v in enumerate(rank):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.4)
