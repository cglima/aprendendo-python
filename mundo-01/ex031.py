"""EXERCÍCIO 031 - CUSTO DA VIAGEM
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
e R$0,45 para viagens mais longas.
"""

distancia = float(input('Qual a distância da viagem em km? '))

'''if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45'''

#condição simplificada
passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A passagem custa R${:.2f}'.format(passagem))

