"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
cc = 0
while True:
    c = randint(1, 2)
    j = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    while j not in 'PI':
        print('\033[31mErro!\033[m Insira um valor válido:')
        j = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    jj = int(input('[1/2]? '))
    while jj != 1 and jj != 2:
        print('\033[31mErro!\033[m Insira um valor válido:')
        jj = int(input('[1/2]? '))
    if j == 'P' and jj == 1 and c == 1:
        print(f'\033[32mParabéns, você venceu!\033[m Você jogou {jj} e o computador {c}, jogue novamente:')
        cc += 1
    elif j == 'P' and jj == 2 and c == 2:
        print(f'\033[32mParabéns, você venceu!\033[m Você jogou {jj} e o computador {c}, jogue novamente:')
        cc += 1
    elif j == 'P' and jj == 1 and c == 2:
        print(f'\033[31mGAME OVER!\033[m Você jogou {jj}, o computador jogou {c} e você venceu {cc} vezes.')
        break
    elif j == 'P' and jj == 2 and c == 1:
        print(f'\033[31mGAME OVER!\033[m Você jogou {jj}, o computador jogou {c} e você venceu {cc} vezes.')
        break
    elif j == 'I' and jj == 1 and c == 2:
        print(f'\033[32mParabéns, você venceu!\033[m Você jogou {jj} e o computador {c}, jogue novamente:')
        cc += 1
    elif j == 'I' and jj == 2 and c == 1:
        print(f'\033[32mParabéns, você venceu!\033[m Você jogou {jj} e o computador {c}, jogue novamente:')
        cc += 1
    elif j == 'I' and jj == 1 and c == 1:
        print(f'\033[31mGAME OVER!\033[m Você jogou {jj}, o computador jogou {c} e você venceu {cc} vezes.')
        break
    elif j == 'I' and jj == 2 and c == 2:
        print(f'\033[31mGAME OVER!\033[m Você jogou {jj}, o computador jogou {c} e você venceu {cc} vezes.')
        break
