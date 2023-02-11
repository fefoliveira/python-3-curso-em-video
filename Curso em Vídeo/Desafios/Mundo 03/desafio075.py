"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

tupla = (int(input(f'Digite o 1º número: ')), int(input(f'Digite o 2º número: ')),
         int(input(f'Digite o 3º número: ')), int(input(f'Digite o 4º número: ')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro número 3 foi digitado na posição {tupla.index(3) + 1}.')
print(f'Os números pares foram: ', end='')
for c in range(len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
