"""
# desafio111:
Crie um pacote chamado "utilidadescev" que tenha dois módulos internos chamados moedas e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
e mantenha tudo funcionando.

# desafio112:
Dentro do pacote "utilidadescev" que criamos no desafio111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas
com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
