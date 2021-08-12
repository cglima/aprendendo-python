"""EXERCÍCIO 018 - SENO, COSSENO E TANGENTE
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tang = tan(radians(angulo))

print('O seno de {}° é {:.2f}'.format(angulo, seno))
print('O cosseno de {}° é {:.2f}'.format(angulo, cosseno))
print('A tangente de {}° é {:.2f}'.format(angulo, tang))