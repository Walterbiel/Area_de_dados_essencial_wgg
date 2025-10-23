# Realizar INNER JOIN entre tabelas

## Descrição
Mostra como combinar dados de pedidos e clientes para trazer informações complementares.

## Código
```sql
SELECT p.id_pedido,
       c.nome AS cliente,
       p.valor
FROM pedidos p
INNER JOIN clientes c ON c.id_cliente = p.id_cliente;
```

## Explicação passo a passo
1. Identifique a coluna em comum entre as tabelas (id_cliente).
2. Escreva a consulta utilizando INNER JOIN.
3. Selecione as colunas desejadas de cada tabela com alias.
4. Execute e confirme se cada pedido está vinculado ao cliente correto.
5. Aplique filtros adicionais se necessário.

## Resultado esperado
A consulta retorna pedidos acompanhados do nome do cliente responsável por cada transação.
