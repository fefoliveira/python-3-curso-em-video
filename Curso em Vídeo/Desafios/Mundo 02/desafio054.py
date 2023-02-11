"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores.
Obs.: Considere a maioridade como 21 anos."""

from datetime import date
aa = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = aa - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade, e {} pessoas menores de idade.'.format(tmaior, tmenor))
