# Agrupar e agregar dados

## Descrição
Demonstra como calcular receita total por categoria usando groupby.

## Código
```python
receita_categoria = vendas.groupby("categoria")["valor"].sum()
print(receita_categoria)
```

## Explicação passo a passo
1. Use groupby para agrupar por categoria.
2. Selecione a coluna numérica e aplique sum().
3. Converta o resultado em DataFrame com reset_index() se necessário.
4. Ordene os valores com sort_values().
5. Exporte o resultado para CSV com to_csv().

## Resultado esperado
Um resumo por categoria mostra quanto cada grupo faturou, ajudando na priorização de produtos.
