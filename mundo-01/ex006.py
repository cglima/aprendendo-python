"""
EXERCÍCIO 006 - DOBRO, TRIPLO E RAIZ QUADRADA
Crie um algoritmo que leia um número e mostre o seu dobro, triplo
e raiz quadrada.
"""
n = int(input('Digite um número: '))

#dobro do número
dobro = 2 * n
#triplo do número
triplo = 3 * n
#raiz quadrada do número
raiz = float(n) ** 0.5

print('\n O número é {} \n O dobro desse número é {} \n O triplo desse numero é {} \n E a raiz quadrada é {:.3} \n' .format(n, dobro, triplo, raiz))