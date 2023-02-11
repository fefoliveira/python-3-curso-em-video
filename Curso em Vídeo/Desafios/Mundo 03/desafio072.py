"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrálo por extenso."""

from time import sleep
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while not 0 <= n <= 20:
        n = int(input('\033[31mErro!\033[m Insira número APENAS ENTRE 0 E 20: '))
    print(f'O número \033[33m{n}\033[m é escrito por extenso como \033[33m"{tupla[n]}"\033[m.')
    sleep(1)
    c = str(input('Você gostaria de inserir mais um número? [S/N]: ')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('\033[31mErro!\033[m Insira somente "S" ou "N": ')).strip().upper()[0]
    if c == 'N':
        break
print('\033[31mFim do programa.\033[m')
