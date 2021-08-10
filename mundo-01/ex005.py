"""
EXERCÍCIO 005 - Antecessor e Sucessor
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.
"""
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('\n O número digitado foi o {} \n O seu sucessor é o {} \n'
.format(numero, sucessor), end= ' ')
print('O seu antecessor é o {} \n' .format(antecessor))

#OUTRO METODO
print('\n Outro método de resolução!!! \n')

n = int(input('Digite um número: '))
print('O numero escolhido é {},\n seu antecessor é {}  \ne o sucessor é {}'.format(n, (n-1), (n+1)))