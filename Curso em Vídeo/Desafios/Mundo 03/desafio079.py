"""Crie um programa onde o usuário pode digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número digitado já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

lista = []
while True:
    aux = int(input('Digite um número (0 para parar): '))
    while aux in lista:
        aux = int(input('\033[31mNúmero inválido!\033[m Digite um número que não foi digitado (0 para parar): '))
    if aux == 0:
        break
    lista.append(aux)
lista.sort()
print(f'Os números únicos digitados foram: \033[35m{lista}\033[m')
