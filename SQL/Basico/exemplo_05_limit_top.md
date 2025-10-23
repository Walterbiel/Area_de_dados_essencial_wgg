# Limitar número de linhas retornadas

## Descrição
Demonstra como trazer apenas os 5 primeiros registros usando LIMIT.

## Código
```sql
-- Retorna apenas 5 registros
SELECT *
FROM clientes
LIMIT 5;
```

## Explicação passo a passo
1. Escreva a consulta desejada.
2. Adicione LIMIT 5 ao final (ou TOP 5 em SQL Server).
3. Execute e observe que apenas 5 linhas são retornadas.
4. Ajuste o número conforme necessário.
5. Combine com ORDER BY para definir quais registros aparecem.

## Resultado esperado
Somente os cinco primeiros registros são exibidos, útil para amostragens rápidas.
