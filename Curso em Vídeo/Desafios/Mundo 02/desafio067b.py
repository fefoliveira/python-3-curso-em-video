n = 0
while True:
    n = int(input('\033[33mDigite um número inteiro e positivo para ver sua tabuada (negativo para sair): \033[m'))
    if n < 0:
        break
    for c in range(0, 10):
        c += 1
        print(f'{n} x {c} = {n * c}')
print('\033[31mFim do programa.\033[m')
