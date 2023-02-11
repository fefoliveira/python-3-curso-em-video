"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 1834
unidade: 4
dezenha: 3
centena: 8
milhar: 1"""

#num = str(input('Digite um número de até quatro dígitos: '))
#print("""Unidade: {};
#Dezena: {};
#Centena: {};
#Milhar: {}.""".format(num[3], num[2], num[1], num[0]))

num = int(input('Digite um número de até quatro dígitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Unidade: {};
Dezena: {};
Centena: {};
Milhar: {}.""".format(u, d, c, m))
