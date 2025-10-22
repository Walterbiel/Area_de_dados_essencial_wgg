# Consumir API com requests

## Descrição
Mostra como buscar dados de uma API pública e converter para DataFrame.

## Código
```python
import requests

response = requests.get("https://api.exemplo.com/produtos")
dados = response.json()
produtos_df = pd.DataFrame(dados)
print(produtos_df.head())
```

## Explicação passo a passo
1. Instale a biblioteca requests.
2. Realize uma requisição GET para a API desejada.
3. Converta a resposta JSON em dicionário Python.
4. Crie um DataFrame com pd.DataFrame.
5. Trate erros verificando response.status_code.

## Resultado esperado
Os dados retornados pela API são convertidos em DataFrame, prontos para análise.
