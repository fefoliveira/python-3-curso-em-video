cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto e branco': '\033[7;30m'}

nome = 'Fernando'
# nome = str(input('Qual o seu nome? '))
print('Olá! Muito prazer em te cohecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
