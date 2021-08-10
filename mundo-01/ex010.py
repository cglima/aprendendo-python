"""
EXERCÍCIO 010 - CONVERSOR DE MOEDAS
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar
"""
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.19
euro = real / 6.08
libra = real / 7.18

print('Você tem R${:.2f} na carteira! ' .format(real))
print('Hoje o dólar vale R${} e você pode comprar US${:.2f} ' .format(5.19, dolar))
print('Hoje o euro vale R${} e você pode comprar €{:.2f}' .format(6.08, euro))
print('Hoje a libra esterlina vale R${} e você pode comprar £{:.2f}' .format(7.18, libra))

