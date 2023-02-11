"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""

n = int(input('\033[33mDigite a quantia de números que você deseja ver da sequência de Fibonacci:\033[m '))
if n == 1:
    print('0 -> ', end='')
elif n == 2:
    print('0 -> 1 -> ', end='')
elif n == 3:
    print('0 -> 1 -> 1 -> ', end='')
elif n == 4:
    print('0 -> 1 -> 1 -> 2 -> ', end='')
elif n == 5:
    print('0 -> 1 -> 1 -> 2 -> 3 -> ', end='')
elif n == 6:
    print('0 -> 1 -> 1 -> 2 -> 3 -> 5 -> ', end='')  # Tive que colocar os 6 primeiros termos fora do laço pois o laço só conta o n solicitado em cima dos 3 primeiros números. Ex.: n = 4, vão ser mostrados os 7 primeiros termos
else:
    t1 = 0  # Primeiro termo da sequência de Fibonacci
    t2 = 1  # Segundo termo da sequência de Fibonacci
    print('{} -> {} -> '.format(t1, t2), end='')
    c = 0
    while c <= n:
        t3 = t1 + t2
        print('{} -> '.format(t3), end='')
        t1 = t2
        t2 = t3  # Faz com que o t1 tome o lugar do t2, e o t2 tome o lugar do t3, pra conseguir somar a próxima casa da sequência quando repetir o laço
        c += 1
print('\033[31mFim\033[m.')
