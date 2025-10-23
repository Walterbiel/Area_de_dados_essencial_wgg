# Criar medida DAX no Power Pivot

## Descrição
Aprenda a escrever uma medida DAX para calcular a margem de lucro diretamente no modelo de dados.

## Código
```dax
Margem % := DIVIDE(SUM(FatoVendas[Lucro]); SUM(FatoVendas[Receita]))
```

## Explicação passo a passo
1. Abra o Power Pivot e acesse a tabela FatoVendas.
2. Na barra de fórmulas, crie uma nova medida com o código indicado.
3. Nomeie a medida como Margem %.
4. Use a medida em uma Tabela Dinâmica para comparar margens por categoria.
5. Formate a medida como porcentagem com uma casa decimal.

## Resultado esperado
A medida Margem % fica disponível para todas as análises que utilizem o modelo de dados.
