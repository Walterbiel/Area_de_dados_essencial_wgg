# Treinar modelo de regressão com scikit-learn

## Descrição
Demonstra como construir pipeline de regressão linear para prever receita.

## Código
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

features = vendas[["investimento_marketing", "numero_clientes"]]
alvo = vendas["receita"]

X_train, X_test, y_train, y_test = train_test_split(features, alvo, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
previsoes = modelo.predict(X_test)
rmse = mean_squared_error(y_test, previsoes, squared=False)
print(f"RMSE: {rmse:.2f}")
```

## Explicação passo a passo
1. Separe variáveis explicativas e alvo.
2. Divida dados em treino e teste com train_test_split.
3. Treine modelo LinearRegression.
4. Gere previsões e calcule RMSE.
5. Avalie necessidade de features adicionais ou normalização.

## Resultado esperado
O modelo gera previsões de receita e o RMSE indica o erro médio das estimativas.
