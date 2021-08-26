#Exemplo 1
nome = str(input('Qual é seu nome? '))
if nome == 'Cassiana':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é bem comum!')
print('Bom dia, {}'.format(nome))

#Exemplo 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {.:f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#condição simplificada
#print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')