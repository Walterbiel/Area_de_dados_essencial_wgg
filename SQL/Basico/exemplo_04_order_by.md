# Ordenar resultados com ORDER BY

## Descrição
Aprenda a ordenar clientes alfabeticamente pelo nome.

## Código
```sql
-- Ordena os clientes por nome
SELECT nome, cidade
FROM clientes
ORDER BY nome ASC;
```

## Explicação passo a passo
1. Escreva a consulta básica selecionando as colunas desejadas.
2. Inclua ORDER BY nome ASC ao final.
3. Execute a consulta e valide a ordenação.
4. Troque para DESC para ver ordem decrescente.
5. Combine com múltiplas colunas se precisar de ordenação secundária.

## Resultado esperado
Os clientes são listados em ordem alfabética crescente pelo nome.
