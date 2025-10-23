# Filtrar dados com condições

## Descrição
Ensina a selecionar apenas vendas de determinado estado usando filtros booleanos.

## Código
```python
filtro_sp = vendas[vendas["estado"] == "SP"]
print(filtro_sp.head())
```

## Explicação passo a passo
1. Partindo do DataFrame vendas, aplique condição em uma coluna.
2. Crie uma nova variável para armazenar o resultado filtrado.
3. Visualize as primeiras linhas com head().
4. Conte quantos registros foram filtrados usando len().
5. Combine múltiplas condições com operadores & e |.

## Resultado esperado
Somente as vendas de São Paulo são exibidas, permitindo análises segmentadas.
