# Analisar variação com LAG e LEAD

## Descrição
Utilize funções de janela LAG e LEAD para comparar vendas entre períodos consecutivos.

## Código
```sql
SELECT data_venda,
       valor,
       LAG(valor) OVER (ORDER BY data_venda) AS venda_anterior,
       valor - LAG(valor) OVER (ORDER BY data_venda) AS variacao
FROM vendas_diarias;
```

## Explicação passo a passo
1. Ordene os dados por data para garantir sequência correta.
2. Use LAG para acessar o valor do período anterior.
3. Calcule a diferença entre o valor atual e o anterior.
4. Aplique filtros para destacar aumentos ou quedas acima de determinado percentual.
5. Visualize os resultados em gráficos para melhor interpretação.

## Resultado esperado
A consulta mostra a variação diária de vendas, permitindo identificar tendências e anomalias.
