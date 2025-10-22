# Definir funções reutilizáveis

## Descrição
Mostra como criar uma função que calcula desconto em um preço.

## Código
```python
def calcular_desconto(preco, percentual):
    '''Retorna o preço com desconto aplicado.'''
    desconto = preco * (percentual / 100)
    return preco - desconto

valor_final = calcular_desconto(200, 10)
print(f"Preço final: R$ {valor_final:.2f}")
```

## Explicação passo a passo
1. Defina uma função com parâmetros preço e percentual.
2. Calcule o valor de desconto.
3. Retorne o preço final.
4. Chame a função com valores de exemplo.
5. Imprima o resultado formatado.

## Resultado esperado
O valor do produto com desconto é calculado e exibido, mostrando como reutilizar lógica.
