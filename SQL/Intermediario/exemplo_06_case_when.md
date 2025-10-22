# Classificar resultados com CASE WHEN

## Descrição
Aprenda a criar colunas calculadas que classificam pedidos em faixas de valor.

## Código
```sql
SELECT id_pedido,
       valor,
       CASE
           WHEN valor < 500 THEN 'Baixo'
           WHEN valor < 2000 THEN 'Médio'
           ELSE 'Alto'
       END AS faixa_valor
FROM pedidos;
```

## Explicação passo a passo
1. Escreva a consulta selecionando o valor do pedido.
2. Use CASE WHEN para definir faixas personalizadas.
3. Forneça um alias para a nova coluna (faixa_valor).
4. Execute e valide se as classificações estão corretas.
5. Ajuste os limites conforme contexto do negócio.

## Resultado esperado
Cada pedido recebe uma etiqueta de faixa de valor, útil para segmentações e relatórios.
