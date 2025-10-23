# Selecionar colunas específicas

## Descrição
Demonstra como limitar o resultado a colunas relevantes para análise.

## Código
```sql
-- Retorna apenas nome e cidade dos clientes
SELECT nome, cidade
FROM clientes;
```

## Explicação passo a passo
1. Identifique as colunas necessárias (nome e cidade).
2. Escreva a consulta selecionando apenas essas colunas.
3. Execute a consulta no banco.
4. Observe que apenas as colunas escolhidas são exibidas.
5. Use esta técnica para reduzir tráfego de dados.

## Resultado esperado
O resultado mostra somente nome e cidade dos clientes, facilitando consultas objetivas.
