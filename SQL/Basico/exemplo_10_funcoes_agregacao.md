# Calcular agregações simples

## Descrição
Ensina a usar SUM, AVG e COUNT para obter indicadores básicos.

## Código
```sql
-- Indicadores de faturamento
SELECT SUM(valor) AS total_vendas,
       AVG(valor) AS ticket_medio,
       COUNT(*) AS quantidade_pedidos
FROM pedidos;
```

## Explicação passo a passo
1. Identifique a tabela de pedidos e suas colunas numéricas.
2. Use funções de agregação para calcular total, média e contagem.
3. Execute a consulta e analise os indicadores retornados.
4. Combine com WHERE para filtrar por período.
5. Use alias para nomear cada métrica.

## Resultado esperado
O banco retorna indicadores consolidados de vendas, úteis para relatórios executivos.
