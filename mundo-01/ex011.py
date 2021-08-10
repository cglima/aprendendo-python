"""EXERCÍCIO 011 - PINTANDO PAREDE
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

area = (largura * altura)
print('A parede tem dimensão de {}x{} e sua área é de {}m².' .format(largura, altura, area))
tinta = area / 2
print('Serão necessários {}l.' .format(tinta))

