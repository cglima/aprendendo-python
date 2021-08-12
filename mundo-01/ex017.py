"""EXERCÍCIO 017 - CATETOS E HIPOTENUSA
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
import math

coposto = float(input('Qual o comprimento do cateto oposto: '))
cadjacente = float(input('Qual o comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(coposto**2 + cadjacente**2)
print('A hipotenusa é igual a {:.2f}'.format(hipotenusa))

#outra forma
hi = math.hypot(coposto, cadjacente)
print('A hipotenusa é igual a {:.2f}'.format(hi))