"""Modifique as funções que foram criadas no desafio107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio108."""

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}'
      f'\nO dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}'
      f'\nAumentando 10%, temos {moeda.aumentar(p, 10, True)}'
      f'\nReduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
