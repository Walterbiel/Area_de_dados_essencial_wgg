# Filtrar intervalos numéricos com BETWEEN

## Descrição
Demonstra como selecionar pedidos dentro de um intervalo de datas.

## Código
```sql
-- Pedidos emitidos no mês de janeiro
SELECT id_pedido, data_pedido, valor
FROM pedidos
WHERE data_pedido BETWEEN '2023-01-01' AND '2023-01-31';
```

## Explicação passo a passo
1. Defina o intervalo desejado usando datas ou números.
2. Adicione a cláusula BETWEEN início AND fim.
3. Execute a consulta e confirme o período retornado.
4. Lembre-se de que BETWEEN inclui os limites.
5. Combine com ORDER BY para ordenar por data.

## Resultado esperado
A consulta retorna apenas os pedidos emitidos no período especificado.
