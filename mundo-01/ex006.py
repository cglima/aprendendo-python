"""
EXERCÍCIO 006 - DOBRO, TRIPLO E RAIZ QUADRADA
Crie um algoritmo que leia um número e mostre o seu dobro, triplo
e raiz quadrada.
"""
n = int(input('Digite um número: '))

#dobro do número
dobro = n * 2
#triplo do número
triplo = n * 3
#raiz quadrada do número
raiz = n ** (1/2)

print('\n O número é {} \n O dobro desse número é {} \n O triplo desse numero é {} \n E a raiz quadrada é {:.2f} \n' .format(n, dobro, triplo, raiz))

