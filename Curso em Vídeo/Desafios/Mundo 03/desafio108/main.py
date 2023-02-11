"""Adapte o código do desafio107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado"""

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}'
      f'\nO dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}'
      f'\nAumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}'
      f'\nReduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
