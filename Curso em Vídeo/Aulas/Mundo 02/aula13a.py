# print('Oi')
# print('Oi')
# print('Oi')
for c in range(0, 3):  # Repete o "print('Oi')" 3 vezes.
    print('Oi')
print('-' * 10)

for c in range(1, 6):  # Conta de 1 até 5.
    print(c)
print('-' * 10)

for c in range(6, 0, -1):  # Conta até 5 de trás para frente.
    print(c)
print('-' * 10)

for c in range(0, 7, 2):  # Conta de 0 até 6, pulando de 2 em 2.
    print(c)
print('-' * 10)

n = int(input('Digite um número: '))
for c in range(0, n+1):  # Conta de 0 até o número digitado (foi add +1 pra considerar o ultimo)
    print(c)
print('-' * 10)
