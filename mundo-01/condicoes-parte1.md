# Condições Simples e Compostas

## Estrutura condicional (Condição)

Acontece uma situação ou outra, NUNCA as duas ao mesmo tempo:

```python
if carro.esquerda():
    bloco True
else:
    bloco False
```

exemplo:

```python
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
```

## Condição Simplificada

```python
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo <=3 else 'carro velho')
print('--FIM--')
```
