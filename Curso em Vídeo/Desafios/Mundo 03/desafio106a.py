"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário difitar a palavra 'FIM', o programa
se encerrará. Obs.: use cores."""

from time import sleep


def helpy():
    while True:
        print('\033[30;42m', '~' * 32, '\n   SISTEMA DE AJUDA DO PYTHON:\n', '~' * 32, '\n\033[m', end='')
        biblio = str(input('Digite a função ou biblioteca ("FIM" para sair): ')).lower()
        if biblio in 'fim':
            print('\033[30;41m', '~' * 7, '\n   FIM\n', '~' * 7, '\n\033[m')
            break
        else:
            print('\033[30;44m', '~' * 40, f'\n   ACESSANDO O MANUAL DA FUNÇÃO {biblio}:\n', '~' * 40, '\n\033[m', end='')
            for c in range(0, 3):
                sleep(1)
                print('\033[30;44m.', end=' ')
            sleep(1.3)
            print(f'\n\033[30;47m', end='')
            print(help(biblio))
            print('\033[m', end='')
            sleep(2)


helpy()
