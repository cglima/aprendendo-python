"""
EXERCÍCIO 004 - DISSECANDO UMA VARIÁVEL
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

n = input('Digite algo: ')

#tipo primitivo
print('O tipo primitivo desse valor é ', type(n))
print('O tipo primitivo desse valor é {}' .format(type(n)))

#só tem espaços
print('Só tem espaços? ', n.isspace())
print('Só tem espaços? {}' .format(n.isspace()))

#é um número
print('É um número? ', n.isnumeric())
print('É um número? {}' .format(n.isnumeric()))

#é alfabético
print('É alfabético? ', n.isalpha())
print('É alfabético? {}' .format(n.isalpha()))

#é alfanumérico
print('é alfanumérico? ', n.isalnum())
print('é alfanumérico? {}' .format(n.isalnum()))

#está em maiscula
print('Está em maísculas? ', n.isupper())
print('está em maísculas? {}' .format(n.isupper()))

#está em minuscula
print('Está em minúsculas? ', n.islower())
print('está em minúsculas? {}' .format(n.islower()))

#está capitalizada
print('Está capitalizada?', n.istitle())
print('está capitalizada? {}' .format(n.istitle()))