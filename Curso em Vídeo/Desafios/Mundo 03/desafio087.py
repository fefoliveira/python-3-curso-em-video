"""Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados;
    B) A soma dos valores da terceira coluna;
    C) O maior valor da segunda linha"""

matriz = list()
linha = list()
pares = terceira = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor inteiro para a posição [{i}][{j}]: '))
        if valor % 2 == 0:
            pares += valor
        if j == 2:
            terceira += valor
        if i == 1 and valor > maior:
            maior = valor
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

print('\nA matriz digitada foi:')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

print(f'\nA soma de todos os valores pares digitados é: {pares};'
      f'\nA soma dos valores da terceira coluna é: {terceira};'
      f'\nO maior valor da segunda linha é: {maior}.')
