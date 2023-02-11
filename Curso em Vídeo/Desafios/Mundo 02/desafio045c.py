# Código identico ao do Guanabara:
from random import randint
from time import sleep
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 1 ] PEDRA'
[ 2 ] PAPEL'
[ 3 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('-= * 11')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-= * 11')
if computador == 0:  # Computador jogou PEDRA.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[31mERRO!\033[m Opção inválida, tente novamente.')
elif computador == 1:  # Computador jogou PAPEL.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[31mERRO!\033[m Opção inválida, tente novamente.')
elif computador == 2:  # Computador jogou TESOURA.
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[31mERRO!\033[m Opção inválida, tente novamente.')
