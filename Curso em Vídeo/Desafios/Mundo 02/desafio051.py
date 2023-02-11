"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print('Veja os 10 termos de uma PA:')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r  # Fórmula do enézimo termo de uma PA
for c in range(p, d, r):
    print('{}'.format(c), end=' -> ')
print('\033[31mFIM\033[m.')
