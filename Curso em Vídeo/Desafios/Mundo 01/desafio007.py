# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. *Dica: Ordem de precedência.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('A média de suas notas ({} e {}) equivale a {}.'.format(n1, n2, m))
