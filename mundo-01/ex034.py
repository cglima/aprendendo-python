"""EXERCÍCIO 034 - AUMENTOS MÚLTIPLOS
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
seu aumento. Para salários superiores a R$1250,00 calcule, um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual é o seu salário? R$'))

novo = salario + (salario * 10 / 100) if salario > 1250 else salario + (salario * 15 / 100)
print('Você recebeu um aumento. Seu novo salário é igual a R${:.2f}.'.format(novo))

