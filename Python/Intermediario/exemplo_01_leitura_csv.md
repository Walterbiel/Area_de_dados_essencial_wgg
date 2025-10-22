# Ler arquivos CSV com pandas

## Descrição
Mostra como carregar dados de vendas usando pandas e visualizar as primeiras linhas.

## Código
```python
import pandas as pd

# Carrega arquivo CSV para um DataFrame
vendas = pd.read_csv("dados/vendas.csv")
print(vendas.head())
```

## Explicação passo a passo
1. Instale o pandas caso necessário (pip install pandas).
2. Importe o módulo e leia o arquivo CSV.
3. Use head() para visualizar as primeiras linhas.
4. Confirme tipos de dados com vendas.dtypes.
5. Investigue registros ausentes com vendas.isna().sum().

## Resultado esperado
O DataFrame exibe as primeiras linhas do arquivo, confirmando que a leitura ocorreu corretamente.
