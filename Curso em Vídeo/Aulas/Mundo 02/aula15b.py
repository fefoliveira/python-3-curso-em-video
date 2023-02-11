n = soma = 0
while True:
    n = (int(input('Digite um número inteiro: ')))
    if n == 999:
        break  # Não precisa da gambiarra de subtrair o 999 da soma, pois o laço encerra antes de somar
    soma += n
# print('A soma equivale a {}.'.format(soma))
print(f'A soma vale vale {s}.')  # O "f" signigica uma f-string, que permite interpolar a variável direto dentro das chaves só com um f na frente das aspas
