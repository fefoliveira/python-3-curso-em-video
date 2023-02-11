def aumentar(valor, aum, form=False):
    valor = valor + (valor * (aum / 100))
    if not form:
        return valor
    else:
        return f'R${valor}'


def diminuir(valor, dim, form=False):
    valor = valor - (valor * (dim / 100))
    if not form:
        return valor
    else:
        return f'R${valor}'


def dobro(valor, form=False):
    if not form:
        return valor * 2
    else:
        return f'R${valor * 2}'


def metade(valor, form=False):
    if not form:
        return valor * 2
    else:
        return f'R${valor / 2}'


def moeda(valor):
    return f'R${valor}'
