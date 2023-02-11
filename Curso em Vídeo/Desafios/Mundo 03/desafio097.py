"""Faça um programa que tenha uma função chamada escreva(), que receba um texsto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.

Ex.:
    escreva('Olá, Mundo!')
Saída:
    -------------
     Olá, Mundo!
    -------------
"""


def escreva(frase):
    print()
    print('-' * (len(frase) + 2))
    print(f' {frase} ')
    print('-' * (len(frase) + 2))


escreva(str(input('Digite uma frase: ')))
