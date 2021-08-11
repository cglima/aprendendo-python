"""EXERCÍCIO 013 - REAJUSTE SALARIAL
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.
"""
salario = float(input('Qual é o salário do funcionário? R$'))

novo = salario + (salario * 15/100)

print('O salario inicial era de R${:.2f}. Com  15% de aumento, passa a receber R${:.2f}' .format(salario, novo))