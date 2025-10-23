# Mesclar consultas no Power Query

## Descrição
Combine duas tabelas relacionadas para enriquecer o conjunto de dados com informações adicionais.

## Código
```m
let
    Vendas = Excel.CurrentWorkbook(){[Name="TabelaVendas"]}[Content],
    Produtos = Excel.CurrentWorkbook(){[Name="DimProduto"]}[Content],
    Fusao = Table.NestedJoin(Vendas, {"IdProduto"}, Produtos, {"IdProduto"}, "Detalhes", JoinKind.LeftOuter),
    Expandido = Table.ExpandTableColumn(Fusao, "Detalhes", {"Categoria", "Marca"})
in
    Expandido
```

## Explicação passo a passo
1. Carregue TabelaVendas e DimProduto para o Power Query.
2. Use Página Inicial > Mesclar Consultas.
3. Selecione a coluna IdProduto em ambas as tabelas.
4. Escolha junção à esquerda para manter todas as vendas.
5. Expanda as colunas Categoria e Marca e carregue o resultado.

## Resultado esperado
A tabela final inclui informações de produto sem duplicar registros, enriquecendo análises e relatórios.
