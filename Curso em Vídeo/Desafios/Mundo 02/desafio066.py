"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada (flag).
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

n = c = s = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma entre eles equivale a {s}.')
