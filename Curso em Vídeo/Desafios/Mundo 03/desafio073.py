"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol (Brasileirão), na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense"""  # Vou fazer do Inter foda-se.
# Tabela usada do dia 15/07/2022

tupla = ('Palmeiras', 'Corinthians', 'Internacional', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'São Paulo',
         'Santos', 'Flamengo', 'Botafogo', 'Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Avaí',
         'Ceará SC', 'Atlético-GO', 'Juventude', 'Fortaleza')
print(f'Os 5 primeiros colocados do Brasileirão são, respectivamente: {tupla[0:5]}')
print(f'Os últimos 4 colocados do Brasileirão são, respectivamente: {tupla[16:20]}')
print(f'A tabela Brasileirão Série A em ordem alfabética fica: {sorted(tupla)}')
print(f'O Internacional de Porto Alegre está na {len(tupla[0:3])}ª posição do Brasileirão.')
