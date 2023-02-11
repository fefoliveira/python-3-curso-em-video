"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""

t = mil = mp = cc = 0
b = ''
while True:
    n = str(input('Digite o nome do produto: ')).rstrip().lstrip()
    p = float(input('Digite o preço desse produto: R$ '))
    cc += 1
    t += p
    if p >= 1000:
        mil += 1
    if cc == 1 or p < mp:
        mp = p
        b = n
#    else:
#        if p < mp:
#            mp = p
#            b = n
    c = str(input('Você gostaria de inserir mais dados? [S/N]: ')).strip().upper()[0]
    while c not in 'SN':
        print('\033[31mErro!\033[m Insira os dados novamente:')
        c = str(input('Você gostaria de inserir mais dados? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        print(f'O total gasto na compra foi de R${t:.2f}, '
              f'foram registrados {mil} produtos que custam mais de R$1000,00 '
              f'e o produto mais barato foi o(a) {b} que custou R${mp:.2f}.')
        break
