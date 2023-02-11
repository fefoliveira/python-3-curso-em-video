"""Aprimore o desafio093 para quie ele funcione com vários jogadores, incluindo um sistema de vizualização de
detalhes do aproveitamento de cada jogador."""

jogadores = list()
jogador = dict()
partidas = list()
cont = 0
while True:
    cont += 1
    jogador['nome'] = str(input(f'Digite o nome do {cont}º jogador: ')).capitalize()
    num = int(input(f'Digite quantas em partidas {jogador["nome"]} atuou: '))
    for c in range(0, num):
        partidas.append(int(input(f'Digite quantos gols {jogador["nome"]} marcou no {c+1}º jogo: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    jogadores.append(jogador.copy())
    continua = str(input('Deseja cadastrar mais um jogador? [S/N]: ')).upper()
    while continua not in 'SN':
        continua = str(input('Inválido! Deseja cadastrar mais um jogador? [Digite apenas S/N]: ')).upper()
    print()
    if continua == 'N':
        break
maior_nome = 0
mais_gols = 0
for c in range(0, len(jogadores)):
    if c == 0:
        maior_nome = len(jogadores[c]['nome'])
        mais_gols = len(jogadores[c]['gols'])
    else:
        if len(jogadores[c]['nome']) > maior_nome:
            maior_nome = len(jogadores[c]['nome'])
        if len(jogadores[c]['gols']) > mais_gols:
            mais_gols = len(jogadores[c]['gols'])
print('cód  nome', end='')
for c in range(0, maior_nome):
    print(end=' ')
print('gols', end='')
for c in range(0, (4 + (mais_gols * 3)) - 4):
    print(end=' ')
print('total')
print('-' * 40)
for c in range(0, len(jogadores)):
    print(f'  {c}  {jogadores[c]["nome"]}', end='')
    for i in range(0, 4 + (maior_nome - len(jogadores[c]['nome']))):
        print(end=' ')
    print(f'{jogadores[c]["gols"]}', end='')
    for i in range(0, (4 + (mais_gols * 3)) - (len(jogadores[c]['gols'] * 3))):
        print(end=' ')
    print(f'{jogadores[c]["total"]}')
while True:
    continua = int(input('\nDeseja mostrar o rendimento de qual jogador? (999 para parar): '))
    if continua != 999:
        while continua < 0 or 999 > continua > (len(jogadores) - 1) or continua > 999:
            continua = int(input('Inválido! Informe novamente o código do jogador que deseja mostrar (999 para parar): '))
        if continua != 999:
            print('-' * 40)
            print(f'Levantamento do jogador {jogadores[continua]["nome"]}:')
            for c in range(0, len(jogadores[continua]['gols'])):
                print(f'  No {c+1}º jogo fez {len(jogadores[continua]["gols"])} gols.')
        else:
            break
    else:
        break
print('\033[31mFIM DO PROGRAMA\033[m')
