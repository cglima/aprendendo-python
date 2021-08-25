"""EXERCÍCIO 023 - SEPARANDO DÍGITOS DE UM NÚMERO
Faça um programa que leia um número de 0 a 9999 e mostre a tela cada um dos digitos separados.
"""

#numero = int(input('Digite um número de 0 a 9999: '))
#n = str(numero)
#print('Analisando o número {}'.format(numero))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
#pra este caso precisa de utilizar ferramentas de repetição, pois ao digitar um numero com 3 digitos, dá erro esta aplicação.


numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
