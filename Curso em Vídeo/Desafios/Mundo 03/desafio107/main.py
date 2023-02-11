"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade().
Faça também um programa que importe esse modo e use algumas dessas funções"""

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}'
      f'\nO dobro de {p} é {moeda.dobro(p)}'
      f'\nAumentando 10%, temos {moeda.aumentar(p, 10)}'
      f'\nReduzindo 13%, temos {moeda.diminuir(p, 13)}')
