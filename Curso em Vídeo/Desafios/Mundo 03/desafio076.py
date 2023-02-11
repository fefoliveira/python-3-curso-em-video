"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, orgasnizando-os dados em forma tabular."""

tupla = ('Arroz', 21.90, 'Feijão', 9.60, 'Peito de frango', 22.00, 'Leite', 6.70, 'Aveia', 2.20)
cont = 0
for c in range(len(tupla)//2):
    print(f'{tupla[cont]}', end='')
    for i in range(32-len(tupla[cont])):
        print('.', end='')
    print(f' {tupla[cont+1]}')
    cont = cont + 2
