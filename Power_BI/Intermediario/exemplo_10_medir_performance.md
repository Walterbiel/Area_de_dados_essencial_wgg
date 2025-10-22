# Construir gráfico de desempenho vs meta

## Descrição
Crie um gráfico de barras onde a meta é exibida como linha constante para comparação.

## Código
```text
# Medidas necessárias
# Total Vendas = SUM(FatoVendas[Receita])
# Meta Constante = 500000
# Visual: Coluna Clusterizada + Linha constante
```

## Explicação passo a passo
1. Crie medida Meta Constante usando VAR Meta = 500000 RETURN Meta, se preferir.
2. Insira um gráfico de colunas por mês.
3. Adicione Total Vendas como valores.
4. No painel Analítico, inclua Linha Constante com valor 500000 e nome 'Meta'.
5. Formate a linha em vermelho para destaque.

## Resultado esperado
O gráfico mostra rapidamente meses que superaram ou ficaram abaixo da meta fixa.
