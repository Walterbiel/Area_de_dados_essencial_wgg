# Criar gráfico de barras com matplotlib

## Descrição
Demonstra como plotar receita por categoria utilizando gráfico de barras.

## Código
```python
import matplotlib.pyplot as plt

receita_categoria.sort_values(ascending=False).plot(kind="bar", color="skyblue")
plt.title("Receita por Categoria")
plt.ylabel("Receita (R$)")
plt.show()
```

## Explicação passo a passo
1. Importe matplotlib e utilize a série receita_categoria.
2. Ordene os valores para destacar categorias mais importantes.
3. Use plot(kind='bar') para gerar o gráfico.
4. Inclua título e rótulos de eixos.
5. Exiba o gráfico com plt.show().

## Resultado esperado
Um gráfico de barras ilustra a distribuição de receita por categoria de forma visual.
