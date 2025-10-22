# Agrupar resultados por categoria

## Descrição
Demonstra como calcular o total de vendas por categoria de produto.

## Código
```sql
SELECT pr.categoria,
       SUM(p.valor) AS total_categoria
FROM pedidos p
JOIN produtos pr ON pr.id_produto = p.id_produto
GROUP BY pr.categoria;
```

## Explicação passo a passo
1. Identifique a tabela de pedidos e a dimensão produtos.
2. Realize o JOIN entre as tabelas usando a chave id_produto.
3. Use SUM para somar o valor das vendas.
4. Agrupe por categoria para consolidar os resultados.
5. Ordene o resultado decrescentemente para destacar as categorias mais rentáveis.

## Resultado esperado
A consulta apresenta o total de vendas por categoria de produto, útil para relatórios gerenciais.
