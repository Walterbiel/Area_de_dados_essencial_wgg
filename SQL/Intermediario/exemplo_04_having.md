# Filtrar agregações com HAVING

## Descrição
Aprenda a exibir apenas categorias com vendas acima de um valor mínimo.

## Código
```sql
SELECT pr.categoria,
       SUM(p.valor) AS total_categoria
FROM pedidos p
JOIN produtos pr ON pr.id_produto = p.id_produto
GROUP BY pr.categoria
HAVING SUM(p.valor) > 50000;
```

## Explicação passo a passo
1. Monte a consulta com GROUP BY como no exemplo anterior.
2. Adicione a cláusula HAVING para filtrar agregações.
3. Defina o limite mínimo desejado (50000).
4. Execute e observe apenas categorias que superam o valor.
5. Ajuste o limite conforme necessidade do negócio.

## Resultado esperado
Somente categorias com faturamento superior a 50 mil são exibidas, destacando principais produtos.
