"""
EXERCÍCIO 008 - CONVERSOR DE MEDIDAS
Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.
"""
medida = float(input('Digite uma distância em metros: '))


km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m equivale a: \n {:.0f}km, {:.0f}hm, {:.0f}dam, {:.0f}dm, {:.0f}cm e {:.0f}mm'. format(medida, km, hm, dam, dm, cm, mm))
