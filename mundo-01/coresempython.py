#print('\033[4;30;45mOlá, mundo!\033[m')

#print('\033[7;30mOlá, mundo!\033[m')

#print('\033[7;33;44mOlá, mundo!\033[m')

#a = 3
#b = 5
#print('Os valores são \033[35m{}\033[m e \033[31m{}\033[m'.format(a, b))

#outro modo
#nome = 'Ciana'
#print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome, '\033[m'))

## mais organizado
nome = 'Ciana'
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'amarelo':'\033[33m',
'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome, cores['limpa']))
print(f'Olá {cores["amarelo"]}! Muito prazer em te conhecer, {nome}{cores["limpa"]}!!!')