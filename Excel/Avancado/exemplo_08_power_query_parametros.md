# Usar parâmetros no Power Query para filtros dinâmicos

## Descrição
Crie parâmetros que permitem alterar ano ou região filtrada sem editar etapas manualmente.

## Código
```m
let
    AnoSelecionado = Excel.CurrentWorkbook(){[Name="ParametroAno"]}[Content]{0}[Valor],
    Fonte = Excel.CurrentWorkbook(){[Name="TabelaVendas"]}[Content],
    Filtrado = Table.SelectRows(Fonte, each [Ano] = AnoSelecionado)
in
    Filtrado
```

## Explicação passo a passo
1. Crie uma tabela ParametroAno com um único valor na planilha.
2. No Power Query, referencie a tabela para criar um parâmetro.
3. Use o parâmetro em Table.SelectRows conforme o código.
4. Carregue a consulta filtrada de volta ao Excel.
5. Altere o valor do parâmetro na planilha e atualize a consulta.

## Resultado esperado
O conjunto de dados responde ao parâmetro escolhido, agilizando análises por período ou região.
