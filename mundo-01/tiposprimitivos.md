# Tipos primitivos e saída de dados

```python
>>> n1 = input('Digite um número: ')
Digite um número: 2
>>> n2 = input('Digite outro número: ')
Digite outro número: 1
>>> s = n1 + n2
>>> print('A soma vale', s)
A soma vale 21
```

- O resultado desse código nao é o esperado, ou seja, a soma de dois números, pois o sinal de '+' está concatenando os dois números que foram digitados, isto é, agrupando os dois números.
A função 'input' lê a entrada como uma string e se a entrada for um número, esta deve ser convertida de acordo com o tipo de variável desejada.
ex.: int() ou float()

  - Para obter o resultado da soma de dois números digitados pelo usuário é necessário dizer para o "interpretador" qual o tipo de variável que queremos manipular.

## Tipos primitivos

int - números inteiros
float - números reais ou números de ponto fluante
bool - números lógicos ou booleanos
str - valor caracteres ou string

### Exemplos

 int = 7, -4, 0, 9675
 float = 4.5, 0.076, -15.223, 7.0
 bool = True, False
 str = 'Olá', '7.5', '',

## Praticando

```python
>>> n1 = input('Digite um número: ')
>>> print(type(n1))
<class 'str'>
```

- Convertendo a variável de entrada para o tipo inteiro

```python
>>> n1 = int(input('Digite um número: '))
Digite um número: 2
>>> n2 = int(input('Digite outro número: '))
Digite um número: 1
>>> s = n1 + n2
>>> print('A soma vale', s)
A soma vale 3
```

```python
>>> print('A soma entre', n1, 'e', n2, 'vale', s)
A soma entre 2 e 1 vale 3
```

Usando função print() no Python 3.6

```python
>>> print('A soma entre {} e {} vale {}'.format(n1, n2, s))
A soma entre 2 e 1 vale 3
```