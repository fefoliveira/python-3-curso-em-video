"""Faça um programa que mostre a tabuada de váruios números, um de cada vez para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

n = c = 0
while True:
    n = int(input('\033[33mDigite um número inteiro e positivo para ver sua tabuada (negativo para sair): \033[m'))
    if n == 0:
        break
    if n < 0:
        break
    for cc in range(n, n * 11, n):
        c += 1
        print(f'{n} x {c} = {cc}')
if n == 0:
    print('Todo número multiplicado por 0 é igual a 0.')
print('\033[31mFim do programa.\033[m')
