# Cores em Python

## No terminal

Para representar uma cor em python sempre utilize:

- \033[style;text;backm

 Código ANSI

```python
    \033[0;33;44m
```

## Códigos para estilo (style)

- 0 : sem estilo (none)
- 1 :negrito (bold)
- 4 : sublinhado (underline)
- 7 : inverter (negative)

## Códigos para texto

- 30 : branco
- 31 : vermelho
- 32 : verde
- 33 : amarelo
- 34 : azul
- 35 : magenta
- 36 : ciano
- 37 : cinza

## Códigos para fundo

- 40 : branco
- 41 : vermelho
- 42 : verde
- 43 : amarelo
- 44 : azul
- 45 : magenta
- 46 : ciano
- 47 : cinza

Exemplos:

- palavra escrito em branco e fundo vermelho

```python
    \033[0;30;41m
```

- palavra escrito em amarelo sublinhada e fundo azul

```python
    \033[4;33;44m
```

- palavra escrito em magenta em negrito e fundo amarelo

```python
    \033[1;35;43m
```

- palavra escrito em branco e fundo verde

```python
    \033[30;42m
```

- palavra escrito em cinza com fundo preto
  - (configuração padrão do terminal)

```python
    \033[m
```

- palavra escrito em preto com fundo branco

```python
    \033[7;30m
```
