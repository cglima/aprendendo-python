"""EXERCÍCIO 012 - CALCULANDO DESCONTOS
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto
"""
preco = float(input('Qual o preço do produto? R$'))
print('O preço do produto é R${}' .format(preco))
desconto = (preco * 5 / 100)
print('5% de desconto no valor do produto é R${:.2f}'. format(desconto))
novo = preco - desconto
print('O novo valor do produto é R${:.2f}.' .format(novo))


