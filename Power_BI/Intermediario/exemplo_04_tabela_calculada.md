# Criar tabela calculada de calendário

## Descrição
Ensina a gerar uma tabela calendário completa para análises temporais.

## Código
```dax
Calendario =
ADDCOLUMNS(
    CALENDAR(DATE(2021,1,1), DATE(2023,12,31)),
    "Ano", YEAR([Date]),
    "Mes", MONTH([Date]),
    "NomeMes", FORMAT([Date], "MMM")
)
```

## Explicação passo a passo
1. Abra a guia Modelagem e selecione Nova Tabela.
2. Cole a expressão DAX para criar o calendário.
3. Marque a coluna Date como tabela de datas.
4. Relacione o calendário à tabela FatoVendas pelo campo Data.
5. Utilize as colunas Ano e NomeMes em visuais.

## Resultado esperado
O modelo passa a ter uma tabela calendário rica, habilitando filtros temporais consistentes.
