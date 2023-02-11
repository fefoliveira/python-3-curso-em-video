"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

# PROGRAMA FRACASSADO: Desisti do código, ficou muito confuso então não vou levar em consideração
# Vou deixar o código ainda salvo para se um dia eu quiser arrumar, estiver disponível
# Resolução certa do Guanabara no desafio065b

n = int(input('Digite um número inteiro: '))
c = 1
soma = n
maior = menor = 0
t = str(input('Você gostaria de continuar a digitar valores? [S/N]: ')).strip().upper()[0]
while t not in 'SN':
    print('\033[31mErro!\033[m Insira novamente os valores:')
    n = int(input('Digite um número inteiro: '))
    t = str(input('Você gostaria de continuar a digitar valores? [S/N]: ')).strip().upper()[0]
while t == 'S':
    n = int(input('Digite outro número inteiro: '))
    t = str(input('Você gostaria de continuar a digitar valores? [S/N]: ')).strip().upper()[0]
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = soma / c
if t == 'N' and c == 1:
    print('\033[33mVocê digitou somente o número {}.\033[m'.format(n))
    print('\033[31mFim do programa.\033[m')
elif t == 'N' and c > 1:
    print('\033[33mVocê digitou {} valores.'
          '\nA média entre eles é de {:.2f}, o maior valor lido foi {} e o menor {}.\033[m'.format(c, media, maior, menor))
    print('\033[31mFim do programa.\033[m')
elif t not in 'SN':
    print('\033[31mErro!\033[m Reenicie o programa.')
