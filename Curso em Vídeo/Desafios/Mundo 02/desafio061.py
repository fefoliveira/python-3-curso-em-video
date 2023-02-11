"""Refaça o desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('\033[33mVeja os 10 termos de uma PA:\033[m')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r  # Fórmula do enézimo termo de uma PA
t = p
c = 1
while c <= 10:
    print('{}'.format(t), end=' -> ')
    t += r
    c += 1
print('\033[31mFIM\033[m.')
