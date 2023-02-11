from random import randint
from time import sleep
n = randint(0, 10)
print('\033[33mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
j = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
acertou = False
tent = 0
while not acertou:
    print('Infelizmente \033[31mvocê errou\033[m.')
    if j < n:
        print('É um pouco mais...')
    elif j > n:
        print('É um pouco menos...')
    j = int(input('\033[33mTente adivinhar o número que eu pensei novamente:\033[m '))
    print('PROCESSANDO...')
    sleep(1)
    tent += 1
    if j == n:
        acertou = True
        tent += 1
        print('\033[32mParabéns, você acertou!\033[m O número escolhido era {} e você fez {} tentativas.'.format(n, tent))
