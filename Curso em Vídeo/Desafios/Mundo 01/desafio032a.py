"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

ano = int(input('Digite um ano qualquer: '))
a1 = ano % 4
a2 = ano % 100
a3 = ano % 400
if a1 > 0:
    print('O ano de {} ano não é bissexto.'.format(ano))
else:
    if a2 > 0:
        print('O ano de {} ano é bissexto!'.format(ano))
    else:
        if a3 > 0:
            print('O ano de {} ano não é bissexto.'.format(ano))
        else:
            print('O ano de {} ano é bissexto!'.format(ano))
