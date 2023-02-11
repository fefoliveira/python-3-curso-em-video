"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import choice
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
user = str(input('\033[34mJokenpô!\033[m ')).strip().lower()
if pc == 'pedra' and user == 'tesoura':
    print('Ops! Você perdeu. Eu joguei {} e você {}.'.format(pc, user))
elif pc == 'pedra' and user == 'papel':
    print('Parabéns! Você me venceu! Eu joguei {} e você {}.'.format(pc, user))
elif pc == 'papel' and user == 'pedra':
    print('Ops! Você perdeu. Eu joguei {} e você {}.'.format(pc, user))
elif pc == 'papel' and user == 'tesoura':
    print('Parabéns! Você me venceu! Eu joguei {} e você {}.'.format(pc, user))
elif pc == 'tesoura' and user == 'papel':
    print('Ops! Você perdeu. Eu joguei {} e você {}.'.format(pc, user))
elif pc == 'tesoura' and user == 'pedra':
    print('Parabéns! Você me venceu! Eu joguei {} e você {}.'.format(pc, user))
