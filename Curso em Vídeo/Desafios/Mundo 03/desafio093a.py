"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
num = int(input(f'Digite quantas em partidas {jogador["nome"]} atuou: '))
jogador['total'] = 0
for c in range(0, num):
    jogador[f'gol{c}'] = int(input(f'Digite quantos gols {jogador["nome"]} marcou no {c+1}º jogo: '))
    jogador['total'] += jogador[f'gol{c}']
print()
for k, v in jogador.items():
    print(f'{k} = {v}')