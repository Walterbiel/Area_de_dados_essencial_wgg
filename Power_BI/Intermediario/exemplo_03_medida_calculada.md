# Calcular margem de lucro percentual

## Descrição
Demonstra como utilizar a função DIVIDE para evitar erros de divisão ao calcular a margem.

## Código
```dax
Margem % := DIVIDE([Total Lucro]; SUM(FatoVendas[Receita]); 0)
```

## Explicação passo a passo
1. Crie a medida Total Lucro, se ainda não existir.
2. Adicione nova medida com a fórmula Margem %.
3. Ajuste o formato para porcentagem com uma casa decimal.
4. Use a medida em um gráfico de colunas para comparar margens por categoria.
5. Valide os resultados com calculadora externa se necessário.

## Resultado esperado
A medida Margem % mostra a relação entre lucro e receita evitando erros de divisão por zero.
