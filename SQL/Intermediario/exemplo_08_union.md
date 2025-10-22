# Combinar conjuntos com UNION

## Descrição
Aprenda a unir registros de duas tabelas compatíveis, como vendas online e loja física.

## Código
```sql
SELECT data_venda, valor, 'Online' AS canal
FROM vendas_online
UNION ALL
SELECT data_venda, valor, 'Loja' AS canal
FROM vendas_loja;
```

## Explicação passo a passo
1. Garanta que ambas as consultas tenham o mesmo número e tipo de colunas.
2. Use UNION ALL para manter duplicatas quando necessário.
3. Execute e verifique se os registros foram combinados corretamente.
4. Adicione ORDER BY externo para ordenar o resultado final.
5. Use UNION (sem ALL) quando precisar remover duplicidades.

## Resultado esperado
Os dados de vendas online e de loja são combinados em um único conjunto com indicação do canal.
