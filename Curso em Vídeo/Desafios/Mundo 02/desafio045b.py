from random import choice
from time import sleep
lista = [1, 2, 3]
pc = choice(lista)
user = int(input('Suas opções:'
                 '\n[ 1 ] PEDRA'
                 '\n[ 2 ] PAPEL'
                 '\n[ 3 ] TESOURA'
                 '\nQual é a sua jogada? '))

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')

if pc == 1 and user == 3:
    print('Ops! \033[31mVocê perdeu\033[m. Eu joguei pedra e você tesoura.')
elif pc == 1 and user == 2:
    print('Parabéns! \033[32mVocê me venceu\033[m! Eu joguei pedra e você papel.')
elif pc == 2 and user == 1:
    print('Ops! \033[31mVocê perdeu\033[m. Eu joguei papel e você pedra.')
elif pc == 2 and user == 3:
    print('Parabéns! \033[32mVocê me venceu\033[m! Eu joguei papel e você tesoura.')
elif pc == 3 and user == 2:
    print('Ops! \033[31mVocê perdeu\033[m. Eu joguei tesoura e você papel.')
elif pc == 3 and user == 1:
    print('Parabéns! \033[32mVocê me venceu\033[m! Eu joguei tesoura e você pedra.')
elif pc == 1 and user == 1:
    print('Ops! \033[33mEmpatamos\033[m! Eu joguei pedra e você pedra.')
elif pc == 2 and user == 2:
    print('Ops! \033[33mEmpatamos\033[m! Eu joguei papel e você papel.')
elif pc == 3 and user == 3:
    print('Ops! \033[33mEmpatamos\033[m! Eu joguei tesoura e você tesoura.')
else:
    print('\033[31mERRO!\033[m Opção inválida, tente novamente.')
