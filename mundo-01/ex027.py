"""EXERCÍCIO 027 - PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA
Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e último nome separadamente.
"""
nome = str(input('Digite seu nome completo? ')).strip()

separa = nome.split()
#print(separa)

print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[len(separa)-1]))
