# Limpar dados no Power Query com etapas registradas

## Descrição
Use o Power Query para remover linhas vazias, substituir valores e padronizar textos automaticamente.

## Código
```m
let
    Fonte = Excel.CurrentWorkbook(){[Name="TabelaVendas"]}[Content],
    LinhasFiltradas = Table.SelectRows(Fonte, each [Valor] <> null),
    TextoPadronizado = Table.TransformColumns(LinhasFiltradas, {{"Região", Text.Upper}})
in
    TextoPadronizado
```

## Explicação passo a passo
1. Selecione a TabelaVendas e abra Dados > Obter e Transformar > Da Tabela/Intervalo.
2. No Power Query, remova linhas em branco utilizando Filtro em Valor.
3. Use Transformar > Formatar > Maiúsculas para padronizar a coluna Região.
4. Clique em Fechar e Carregar para trazer os dados limpos de volta ao Excel.
5. Agende a atualização sempre que novos dados forem adicionados.

## Resultado esperado
O conjunto de dados retorna ao Excel limpo e padronizado, pronto para relatórios confiáveis.
