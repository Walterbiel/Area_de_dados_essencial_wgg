# Unir tabelas com LEFT JOIN

## Descrição
Aprenda a listar todos os clientes mesmo que não tenham pedidos registrados.

## Código
```sql
SELECT c.nome,
       p.id_pedido,
       p.valor
FROM clientes c
LEFT JOIN pedidos p ON p.id_cliente = c.id_cliente;
```

## Explicação passo a passo
1. Comece listando a tabela principal (clientes).
2. Aplique LEFT JOIN para trazer pedidos quando existirem.
3. Observe que clientes sem pedidos terão valores nulos nas colunas da tabela pedidos.
4. Use COALESCE para substituir nulos, se desejado.
5. Ordene por nome para facilitar a leitura.

## Resultado esperado
Todos os clientes são listados e aqueles sem pedidos aparecem com campos de pedido vazios, facilitando análises de engajamento.
