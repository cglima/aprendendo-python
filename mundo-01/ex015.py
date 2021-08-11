"""EXERCÍCIO 015 - ALUGUEL DE CARROS
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado e a quantidade de dias  pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por
km rodado.
"""

km = float(input('Quantos km  rodados: '))
dias = int(input('Quantos dias alugados: '))
print('O carro alugado percorreu {}km' .format(km))
print('O carro ficou alugado por {} dias' .format(dias))

aluguel = 60 * dias
pkm = 0.15 * km

pagamento = aluguel + pkm
print('O total a pagar é {:.2f}' .format(pagamento))
