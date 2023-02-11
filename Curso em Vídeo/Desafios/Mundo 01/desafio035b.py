n1 = float(input('Digite comprimento de uma reta: '))
n2 = float(input('Digite o comprimento de outra: '))
n3 = float(input('Agora o de mais uma: '))
if n1 < n2 + n3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
