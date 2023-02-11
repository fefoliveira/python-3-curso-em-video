"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no invervalo de 1 até 500."""

soma = 0  # Acumulador
cont = 0  # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # Soma o faz uma soma entre o 0 e todos os valores de c
        # += significa que recebe ele mesmo mais o que vem depois, no caso o c
        cont += 1  # A cada valor que cumpre com o for e com o if, conta +1
print('A soma de todos os {} valores ímpares que são múltiplos de três e que se encontram no invervalo de 1 até 500 é igual a \033[34m{}\033[m.'.format(cont, soma))
