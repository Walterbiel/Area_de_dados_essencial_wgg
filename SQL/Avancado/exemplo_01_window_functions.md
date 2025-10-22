# Aplicar funções de janela para ranking

## Descrição
Demonstra como usar ROW_NUMBER para ranquear vendas por cliente dentro de cada região.

## Código
```sql
SELECT c.regiao,
       c.nome,
       p.valor,
       ROW_NUMBER() OVER (PARTITION BY c.regiao ORDER BY p.valor DESC) AS posicao
FROM pedidos p
JOIN clientes c ON c.id_cliente = p.id_cliente;
```

## Explicação passo a passo
1. Realize o JOIN entre pedidos e clientes para acessar a região.
2. Use ROW_NUMBER com PARTITION BY para reiniciar a contagem por região.
3. Ordene os valores dentro da janela em ordem decrescente.
4. Execute a consulta e observe o ranking de vendas por região.
5. Filtre posicao = 1 para obter os líderes regionais.

## Resultado esperado
Cada venda recebe uma posição dentro de sua região, permitindo identificar top clientes locais.
