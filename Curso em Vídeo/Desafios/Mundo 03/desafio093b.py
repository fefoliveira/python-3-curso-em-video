jogador = dict()
partidas = list()
jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
num = int(input(f'Digite quantas em partidas {jogador["nome"]} atuou: '))
for c in range(0, num):
    partidas.append(int(input(f'Digite quantos gols {jogador["nome"]} marcou no {c+1}º jogo: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print()
for k, v in jogador.items():
    print(f'{k} = {v}')
print(f'\nO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   -> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
