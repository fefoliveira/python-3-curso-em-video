a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Agora mais um: '))

if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menos = c

if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print('Entre esses três números, o maior é {} e o menor {}.'.format(maior, menor))
