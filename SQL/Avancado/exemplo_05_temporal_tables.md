# Usar tabelas temporais para auditoria

## Descrição
Demonstra como consultar histórico de alterações utilizando tabelas temporais do SQL Server.

## Código
```sql
SELECT *
FROM clientes FOR SYSTEM_TIME AS OF '2023-06-01T00:00:00';
```

## Explicação passo a passo
1. Garanta que a tabela clientes esteja configurada como temporal.
2. Use a sintaxe FOR SYSTEM_TIME AS OF com a data desejada.
3. Execute para visualizar os valores válidos naquele instante.
4. Experimente outras opções como BETWEEN e CONTAINED IN.
5. Utilize os resultados para auditoria de dados.

## Resultado esperado
É possível recuperar o estado da tabela em qualquer momento histórico, assegurando rastreabilidade.
