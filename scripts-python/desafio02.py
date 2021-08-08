#DESAFIO 02

"""
Criar um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa
e mostre uma mensagem com a data formata.
exemplo:
    dia = 23
    mes = Jan
    ano = 1981
    Você nasceu no dia 23 de Jan de 1981. Correto?
"""
dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('Em que ano você nasceu? ')

print('Você nasceu no dia', dia, 'de', mes, 'de', ano + '.', 'Correto?' )