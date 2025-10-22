# Extrair dados JSON em SQL

## Descrição
Mostra como desmembrar campos JSON armazenados na tabela de integrações.

## Código
```sql
SELECT id_evento,
       JSON_VALUE(payload, '$.cliente.nome') AS nome_cliente,
       JSON_VALUE(payload, '$.pedido.total') AS valor_pedido
FROM eventos_integracao;
```

## Explicação passo a passo
1. Identifique a coluna JSON (payload).
2. Use JSON_VALUE para extrair campos escalares.
3. Aplique alias claros para cada coluna derivada.
4. Combine com CROSS APPLY OPENJSON quando precisar expandir arrays.
5. Valide se o JSON está bem formatado antes da extração.

## Resultado esperado
As informações contidas no JSON são disponibilizadas em colunas tradicionais para análise.
