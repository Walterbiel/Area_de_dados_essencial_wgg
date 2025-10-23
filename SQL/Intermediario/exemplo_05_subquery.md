# Usar subconsulta para filtrar resultados

## Descrição
Demonstra como identificar pedidos acima da média usando uma subconsulta.

## Código
```sql
SELECT id_pedido, valor
FROM pedidos
WHERE valor > (SELECT AVG(valor) FROM pedidos);
```

## Explicação passo a passo
1. Calcule a média de valor de pedidos com uma subconsulta.
2. Utilize a subconsulta dentro da cláusula WHERE.
3. Execute para retornar pedidos com valor acima da média geral.
4. Combine com ORDER BY para ordenar pelos maiores valores.
5. Ajuste a subconsulta para médias por categoria se necessário.

## Resultado esperado
A consulta destaca pedidos com valor acima da média, ajudando na identificação de grandes vendas.
