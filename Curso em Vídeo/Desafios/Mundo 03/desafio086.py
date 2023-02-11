"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta"""

matriz = list()
linha = list()
for c in range(0, 3):
    for i in range(0, 3):
        valor = int(input(f'Digite um valor inteiro para a posição [{c}][{i}]: '))
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()
print('\nA matriz digitada foi:')
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]}]', end=' ')
    print()
