"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
    -Quantidade de notas
    -A maior nota
    -A menor nota
    -A média da turma
    -A situação (opcional)
Adicione também as docstrings da função."""


def notas(*nota, sit=False):
    """
    -> Diante a quantia indeterminada de notas informadas, mostra qual a maior, qual a menor, a média entre todas
    e a situação geral, caso seja solicitada.
    :param nota: Nota a ser informada (quantidade indeterminada).
    :param sit: Identifica a ausência (ou não) da exibição de todo o dicionário (qual return será feito).
    :return: Se sit=False, retorna somente as notas. Se sit=True, retorna todo o dicionário.
    """
    global cont
    cont = 0
    maior = 0
    menor = 0
    media = 0
    dicionario = dict()
    lista = list()
    for n in nota:
        lista.append(n)
        media += n
        if cont == 0:
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        cont += 1
    media = media/cont
    dicionario['notas'] = lista[:]
    dicionario['qtd'] = cont
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = round(media, 2)
    if sit:
        if media < 6:
            dicionario['sit'] = 'RUIM'
        elif 6 < media < 8:
            dicionario['sit'] = 'BOM'
        elif 8 < media < 10:
            dicionario['sit'] = 'MUITO BOM'
        elif media == 10:
            dicionario['sit'] = 'PERFEITO'
        return dicionario
    else:
        return dicionario['notas']


print(notas(5.5, 2.5, 1.5, sit=True))
