# Criar índices compostos eficientes

## Descrição
Demonstra como criar índices em múltiplas colunas para acelerar filtros combinados.

## Código
```sql
CREATE INDEX idx_pedidos_cliente_data
ON pedidos (id_cliente, data_pedido);
```

## Explicação passo a passo
1. Analise consultas mais executadas para identificar colunas filtradas juntas.
2. Crie índice composto começando pela coluna mais seletiva.
3. Execute novamente a consulta e observe melhora de desempenho.
4. Use ferramentas como pg_stat_statements para monitorar impacto.
5. Reavalie periodicamente índices pouco utilizados.

## Resultado esperado
Consultas que filtram por cliente e data utilizam o índice composto, reduzindo leituras desnecessárias.
