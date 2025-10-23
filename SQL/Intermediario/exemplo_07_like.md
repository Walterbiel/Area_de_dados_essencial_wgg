# Localizar padrões com LIKE

## Descrição
Demonstra como buscar clientes cujo nome inicia com determinada letra.

## Código
```sql
SELECT nome, email
FROM clientes
WHERE nome LIKE 'A%';
```

## Explicação passo a passo
1. Defina o padrão de pesquisa usando % como curinga.
2. Escreva a consulta com LIKE 'A%'.
3. Execute e observe os nomes que começam com A.
4. Use '_' para representar um único caractere se necessário.
5. Combine com UPPER para buscas case insensitive.

## Resultado esperado
Somente clientes cujos nomes começam com a letra A são retornados.
