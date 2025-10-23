# Analisar plano de execução para performance

## Descrição
Aprenda a interpretar planos de execução para identificar gargalos em consultas complexas.

## Código
```sql
EXPLAIN ANALYZE
SELECT pr.categoria,
       SUM(p.valor)
FROM pedidos p
JOIN produtos pr ON pr.id_produto = p.id_produto
GROUP BY pr.categoria;
```

## Explicação passo a passo
1. Use EXPLAIN ou EXPLAIN ANALYZE antes da consulta.
2. Execute e observe operações como Seq Scan ou Index Scan.
3. Identifique etapas mais custosas e considere criar índices.
4. Reescreva a consulta se necessário e compare planos.
5. Documente as melhorias realizadas.

## Resultado esperado
O plano de execução evidencia onde a consulta gasta mais recursos, orientando ajustes de performance.
