"""EXERCÍCIO 024 - VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o
nome "SANTO".
"""
cidade = str(input('Em que cidade vc nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')

