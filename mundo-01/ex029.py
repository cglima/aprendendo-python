"""EXERCÍCIO 029 - RADAR ELETRÔNICO
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por
cada km acima do limite.
"""

velocidade = float(input('Digite a velocidade do carro:'))

if velocidade > 80:
    print('MULTADO!!! Você excedeu a velocidade permitida que é de 80km/h!!!')
    multa = (velocidade - 80) *7
    print('A multa é de R${:.2f}!'.format(multa))
else:
    print('Continue! Cuidado com o excesso de velocidade!! Dirija com segurança')