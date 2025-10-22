# Gerar tabela dinâmica com PIVOT

## Descrição
Aprenda a transformar linhas de categorias em colunas usando PIVOT para comparar canais de venda.

## Código
```sql
SELECT *
FROM (
    SELECT canal, DATEPART(MONTH, data_venda) AS mes, valor
    FROM vendas
) src
PIVOT (
    SUM(valor)
    FOR canal IN ([Online], [Loja], [Representante])
) AS pvt
ORDER BY mes;
```

## Explicação passo a passo
1. Construa uma subconsulta com canal, mês e valor.
2. Aplique PIVOT somando valores por canal.
3. Liste explicitamente os canais no operador IN.
4. Ordene o resultado pelo mês para manter sequência temporal.
5. Use COALESCE para tratar valores nulos, se necessário.

## Resultado esperado
Os valores de vendas por canal passam a ocupar colunas distintas, facilitando comparações mensais.
