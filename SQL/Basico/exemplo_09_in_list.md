# Filtrar múltiplos valores com IN

## Descrição
Mostra como selecionar registros que pertencem a uma lista específica.

## Código
```sql
-- Produtos das categorias selecionadas
SELECT nome_produto, categoria
FROM produtos
WHERE categoria IN ('Eletrônicos', 'Informática', 'Telefonia');
```

## Explicação passo a passo
1. Liste os valores relevantes entre parênteses e separados por vírgula.
2. Inclua a cláusula IN na condição WHERE.
3. Execute a consulta e observe os resultados filtrados.
4. Use NOT IN para excluir categorias.
5. Combine com outras condições para filtros complexos.

## Resultado esperado
O resultado apresenta apenas produtos pertencentes às categorias selecionadas.
