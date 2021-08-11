"""EXERCÍCIO 014 - CONVERSOR DE TEMPERATURAS
Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.
"""
celsius = float(input('Digite uma temperatura para converter de graus Celsius para Fahrenheit: '))

fahrenheit = ((9 * celsius) / 5) + 32
print('A temperatura de {}°C corresponde a {:.2f}°F' .format(celsius, fahrenheit))
#extra
kelvin = celsius + 273.15
print('A temperatura {}°C equivale a {:.2f}K' .format(celsius, kelvin))