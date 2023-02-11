# for c in range(1, 5):
#    n = int(input('Digite o {}º número inteiro: '.format(c)))
# print('\033[31mFim.\033[m')
"""Acima o programa pergunta 4 valores, mas se eu não souber quantos valores eu preciso:"""

n = 1
while n != 0:  # O nome disso é "flag" ou "ponto de parada"
    # Enquanto nao for digitado o valor zero, vai continuar a repetir o laço abaixo:
    n = int(input('Digite um número inteiro: '))
print('\033[31mFim.\033[m')
