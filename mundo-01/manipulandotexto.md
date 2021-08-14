# Manipulando Cadeias de texto

cadeia de caracteres é uma string

frase = 'Curso em Video Python'

O python inicia a contagem de posição em 0.

## Fatiamento

- Fatiar uma string é conseguir pegar pedaços dessa string

Com este comando é possível identificar dentro da cadeia de caracteres a letra que está no índice 9.

frase[9]

Já neste código, o resultado são as letras do índice 9 até o 12

    frase[9:13]

    frase[9:21]

- Começa no 9, pára no 21 e salta de 2 em 2

    frase[9:21:2]

- Inicia do caracter 0

    frase[:5]

- Inicia no caracter 15 e vai até o final

    frase[15:]

- Iniciar no caracter 9, vai até o final e pula de 3 em 3

    frase[9::3]

## Análise

- Verificar o comprimento da string

    ```python
    len(frase)
    ```

- Contar quantas vezes aparece a letra 'o' minúscula

    ```python
    frase.count('o')
    ```

- Contar quantas vezes aparece a letra 'o' minúscula, em um intervalo definido.

    ```python
    frase.count('o',0,13)
    ```

- Quantas vezes ele encontrou a string e mostra a partir de qual caracter está na area fatiada

    ```python
    frase.find('deo')
    ```

- Retornar -1 , significa que nao foi encontrado

    ```python
    frase.find('Android')
    ```

- Dentro da frase existe Curso?  ele retorna True

    ```python
    'Curso' in frase
    ```

## Tranformação

- Troca python por android na cadeia de caracteres

    ```python
    frase.replace('Python','Android')
    ```

- Coloca em maiúscula a string

    ```python
    frase.upper()
    ```

- Coloca em minúscula a string

    ```python
    frase.lower()
    ```

- Todos os caracteres vão pra minúscula e a primeira letra fica em maiúscula a string

    ```python
    frase.captalize()
    ```

- Analisa quantas palavras tem a string e coloca maiúscula o inicio de todas as palavras da string

    ```python
    frase.title()
    ```

- Remove todos os espaços inúteis da string (inicio e fim)

    ```python
    frase.strip()
    ```

- Remove somente os últimos espaços da string

    ```python
    frase.rstrip()
    ```

- Remove somente os espaços da esquerda da string

    ```python
    frase.lstrip()
    ```

## Divisão

- Divide a string em pedaços . cada palavra recebe uma indexação nova, e cria uma lista.

    ```python
    frase.split()
    ```

## Junção

- Juntar todos os elementos de frase com o separador '-', separando cada uma das palavras

    ```python
    '-'.join(frase)
    ```
