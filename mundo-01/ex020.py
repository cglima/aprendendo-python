"""EXERCÍCIO 020 - SORTEANDO UMA ORDEM NA LISTA
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
sorteada.
"""
from random import shuffle

aluno1 = 'Lesada'
aluno2 = 'Bugada'
aluno3 = 'Safira'
aluno4 = 'Espoleta'
alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)
print('A ordem de apresentação dos alunos será: ')
print(alunos)