lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print()
for c in lanche:
    print(f'Eu vou comer {c}.')

print()
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}.')

print()
for p, c in enumerate(lanche):  # Além do lanche, dá a posição do mesmo.
    print(f'Eu vou comer {c} na posição {p}.')
