"""EXERCÍCIO 035 - ANALISANDO TRIÂNGULO v1.0
Desenvolva um programa que leia o comprimento de três retas e diga a usuário se
elas podem ou não formar um triângulo.
"""

print('-='*10, 'ANALISADOR DE TRIÂNGULOS', '=-'*10)

reta1 = float(input('Comprimento da reta 1: '))
reta2 = float(input('Comprimento da reta 2: '))
reta3 = float(input('Comprimento da reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com estes comprimentos de retas, temos um triangulo!')
else:
    print('Não é possivel formar um triângulo com estes comprimentos de retas!')
