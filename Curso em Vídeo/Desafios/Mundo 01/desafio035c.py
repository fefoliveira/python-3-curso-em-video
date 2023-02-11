from math import fabs
n1 = float(input('Digite comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra: '))
n3 = float(input('Agora o de mais uma: '))
# if n1 > fabs(n2 - n3) and n1 < (n2 + n3):
if fabs(n2 - n3) < n1 < (n2 + n3):
    print('É possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
