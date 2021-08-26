""" EXERCICIO 028 - JOGO DA ADIVINHAÇÃO v.1.0
Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

computador = randint(0,5)
#print(num)
print('=' * 10, 'ADIVINHE SE FOR CAPAZ', '=' * 10)
print('''TENTE DESCOBRIR QUAL O NUMERO O COMPUTADOR "PENSOU"!!!!
    Escolha um número inteiro entre 0 e 5''')
jogador = int(input('Qual foi o numero escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você venceu!! Parabéns')
else:
    print('Você perdeu!! O número escolhido pelo computador foi o {}.'.format(computador))
print('Jogue mais uma vez!!!')