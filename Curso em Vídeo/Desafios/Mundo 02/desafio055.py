"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa, em Kg: '))
    if p == 1:  # Se for o primeiro peso: Ambos abaixo são iguais a esse primeiro peso
        # Se só foi fornecido um único valor, o mesmo é o maior e o menor ao mesmo tempo
        maior = peso
        menor = peso
    else:  # Nesse else é onde acontecem as tomadas de posições de maior e menor
        if peso > maior:  # Se o peso em questão for maior que o "maior" anterior:
            maior = peso
        if peso < menor:  # Se for menos que o "menor":
            menor = peso
print(f'O maior peso lido foi de {maior}Kg, e o menor foi de {menor}Kg.')
