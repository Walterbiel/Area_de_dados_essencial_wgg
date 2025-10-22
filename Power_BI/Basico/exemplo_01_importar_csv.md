# Importar arquivo CSV para o Power BI Desktop

## Descrição
Ensina a carregar dados de um arquivo CSV e preparar a tabela no relatório.

## Código
```m
let
    Fonte = Csv.Document(File.Contents("C:/Dados/vendas.csv"),[Delimiter=",", Columns=5, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    Promovidas = Table.PromoteHeaders(Fonte)
in
    Promovidas
```

## Explicação passo a passo
1. Abra o Power BI Desktop e clique em Obter Dados > Texto/CSV.
2. Selecione o arquivo `vendas.csv` e visualize a prévia.
3. Clique em Transformar Dados para abrir o Power Query.
4. Verifique se os cabeçalhos foram promovidos corretamente.
5. Carregue a tabela para o modelo.

## Resultado esperado
Os dados do CSV ficam disponíveis como tabela no Power BI, prontos para visualizações.
