"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex.: Após a sopa;
A sacada da casa;
A torre da derrota;
O lobo ama o bolo;
Anotaram a data da maratona."""

f = str(input('Digite uma frase, sem acentos: ')).strip().upper()
p = f.split()
tj = ''.join(p)
inv = ''
for c in range(len(tj) - 1, -1, -1):
    inv += tj[c]
print('O inverso da frase "{}" é "{}".'.format(tj, inv))
if inv == tj:
    print('A frase digitada \033[32mé\033[m um palíndromo!')
else:
    print('A frase digitada \033[31mnão é\033[m um palíndromo.')
