"""
EXERCÍCIO 005 - Antecessor e Sucessor
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.
"""
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('\n O número digitado foi o {} \n O seu sucessor é o {} \n'
.format(numero, sucessor, antecessor), end= ' ')
print('O seu antecessor é o {} \n' .format(antecessor))