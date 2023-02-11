"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from desafio115.lib.interface import *
from desafio115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    r = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    if r == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif r == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif r == 3:
        fim()
        break

