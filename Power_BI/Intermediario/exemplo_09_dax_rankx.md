# Classificar produtos com RANKX

## Descrição
Demonstra como criar ranking de produtos baseado em vendas.

## Código
```dax
Ranking Produto := RANKX(ALL(DimProduto[Produto]); [Total Vendas];; DESC)
```

## Explicação passo a passo
1. Crie a medida Total Vendas = SUM(FatoVendas[Receita]).
2. Adicione nova medida com RANKX conforme o código.
3. Use a medida em uma tabela com produtos.
4. Ordene a tabela pelo ranking para destacar os melhores.
5. Aplique filtros de categoria para ver rankings específicos.

## Resultado esperado
Cada produto recebe uma posição no ranking global, permitindo foco nos mais relevantes.
