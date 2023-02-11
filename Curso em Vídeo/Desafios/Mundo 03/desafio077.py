"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

tupla = ('Computador', 'Monitor', 'Mouse', 'Teclado', 'Fone')
for c in tupla:
    print(f'\nAs vogais da palavra \033[33m{c}\033[m são: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'\033[32m{letra}\033[m', end=' ')
print()
