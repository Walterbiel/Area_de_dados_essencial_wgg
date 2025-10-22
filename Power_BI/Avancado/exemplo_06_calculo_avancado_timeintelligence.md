# Aplicar cálculo de variação anual com DAX

## Descrição
Utilize funções de inteligência de tempo para comparar resultados com o ano anterior.

## Código
```dax
Vendas Ano Anterior := CALCULATE([Total Vendas]; SAMEPERIODLASTYEAR(DimCalendario[Date]))
Variação % Ano := DIVIDE([Total Vendas] - [Vendas Ano Anterior]; [Vendas Ano Anterior])
```

## Explicação passo a passo
1. Garanta que exista uma tabela calendário marcada como tabela de datas.
2. Crie a medida Vendas Ano Anterior usando SAMEPERIODLASTYEAR.
3. Crie a medida Variação % Ano conforme código.
4. Use ambas em um gráfico de linhas por mês.
5. Interprete os meses com crescimento ou queda.

## Resultado esperado
Relatórios exibem comparação com ano anterior e percentual de variação, apoiando análise de tendências.
