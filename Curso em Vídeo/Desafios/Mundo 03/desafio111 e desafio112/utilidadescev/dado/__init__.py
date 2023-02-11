def leiaDinheiro(frase):
    entrada = str(input(frase)).replace(',', '.').strip()
    while True:
        if entrada.isalpha() or entrada == '':
            entrada = str(input(f'\033[31mEntrada "{entrada}" inválida! Digite apenas valores numéricos racionais '
                                f'positivos: \033[m')).replace(',', '.').strip()
            entrada = float(entrada)
            if entrada > 0:
                break
    return entrada
