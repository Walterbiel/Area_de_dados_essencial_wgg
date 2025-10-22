# Filtrar com operadores AND e OR

## Descrição
Mostra como combinar condições usando operadores lógicos.

## Código
```sql
-- Clientes de São Paulo com compras acima de 500
SELECT nome, cidade, total_compras
FROM clientes
WHERE cidade = 'São Paulo' AND total_compras > 500;
```

## Explicação passo a passo
1. Defina as condições que deseja combinar.
2. Utilize AND para condições que devem ser verdadeiras simultaneamente.
3. Use OR quando qualquer condição puder ser verdadeira.
4. Execute a consulta e valide os resultados.
5. Experimente combinar AND e OR com parênteses.

## Resultado esperado
Somente clientes de São Paulo com compras acima de 500 são exibidos.
