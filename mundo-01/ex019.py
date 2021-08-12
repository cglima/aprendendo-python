"""EXERCÍCIO 019 - SORTEANDO UM ITEM NA LISTA
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o
nome do escolhido.
"""

import random

aluno1 = 'Ciana'
aluno2 = 'Jom'
aluno3 = 'Bugada'
aluno4 = 'Lesada'
lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))

