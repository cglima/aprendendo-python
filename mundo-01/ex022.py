"""EXERCÍCIO 022 - ANALISADOR DE TEXTOS
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o seu nome completo: ')).strip()

maiuscula = nome.upper()
minuscula = nome.lower()

print('O nome completo em maiúscula fica assim: {}'.format(maiuscula))
print('O nome completo em minúscula fica assim: {}'.format(minuscula))

print('O nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

#print('O primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))