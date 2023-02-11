"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

mi = h = mm = 0
while True:
    i = int(input('Digite a idade de uma pessoa: '))
    s = str(input('Digite o sexo biológico dessa pessoa: [M/F]:')).strip().upper()[0]
    while s not in 'MF':
        print('\033[31mErro!\033[m Insira os dados novamente:')
        s = str(input('Digite o sexo biológico dessa pessoa: [M/F]:')).strip().upper()[0]
    if i >= 18:
        mi += 1
    if s == 'M':
        h += 1
    if i < 20 and s == 'F':
        mm += 1
    c = str(input('Você gostaria de inserir mais dados? [S/N]: ')).strip().upper()[0]
    while c not in 'SN':
        print('\033[31mErro!\033[m Insira os dados novamente:')
        c = str(input('Você gostaria de inserir mais dados? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        print(f'\033[33mForam informadas {mi} pessoa(s) com mais de 18 anos, {h} homem(s) e {mm} mulher(es) com menos de 20 anos.\033[m')
        break
