"""Refaça o desafio009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

n = int(input('Digite um número inteiro: '))
print('Segue a tabuada do número {}:'.format(n))
for c in range(n, n * 11, n):
    print(c)
