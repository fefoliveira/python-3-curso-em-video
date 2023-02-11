# Resolução do Guanabara:
from random import randint
v = 0
while True:
    jj = int(input('Digite um valor entre 0 e 10: '))
    c = randint(0, 10)
    tot = j + c
    j = ''
    while j not in 'PI':
        print('\033[31mErro!\033[m Insira um valor válido:')
        j = str(input('\033[33mPar ou ímpar? [P/I]: \033[33m')).strip().upper()[0]
    print(f'Você jogou {jj} e o computador {c}. Total de {tot}, ', end='')
    print('deu par.' if tot % 2 == 0 else 'deu ímpar.')
    if j == 'P':
        if tot % 2 == 0:
            print('\033[32mParabéns, você venceu!\033[m', end='')
        else:
            print('\033[31mGAME OVER!\033[m', end='')
            break
    if j == 'I':
        if tot % 2 == 1:
            print('\033[32mParabéns, você venceu!\033[m', end='')
            v += 1
        else:
            print('\033[31mGAME OVER!\033[m', end='')
            break
    print('Jogue novamente: ')
print(f'Você venceu {c} vezes.')
