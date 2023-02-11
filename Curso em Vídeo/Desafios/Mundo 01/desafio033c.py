a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Agora mais um: '))

# Testando uma das variáveis como o menor/maior antes da estrutura condicional, se pode basear os proximos "ifs" diante desse teste, o que elimina a necessidade de mais uma linha de "if".

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Entre esses três números, o maior é {} e o menor {}.'.format(maior, menor))
