# Filtrar registros com cláusula WHERE

## Descrição
Mostra como recuperar clientes apenas de uma cidade específica.

## Código
```sql
-- Seleciona clientes de São Paulo
SELECT nome, cidade
FROM clientes
WHERE cidade = 'São Paulo';
```

## Explicação passo a passo
1. Defina o critério de filtragem (cidade = 'São Paulo').
2. Adicione a cláusula WHERE à consulta.
3. Execute a consulta e observe os resultados filtrados.
4. Experimente outros valores de cidade para comparar.
5. Combine com operadores lógicos para filtros mais complexos.

## Resultado esperado
A consulta retorna somente os clientes localizados em São Paulo.
