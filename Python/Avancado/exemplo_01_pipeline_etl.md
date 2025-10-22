# Construir pipeline ETL com funções modulares

## Descrição
Mostra como estruturar um fluxo ETL simples com etapas de extração, transformação e carga.

## Código
```python
import pandas as pd

def extrair_dados(caminho_csv):
    '''Lê dados brutos do arquivo de vendas.'''
    return pd.read_csv(caminho_csv)

def transformar_dados(df):
    '''Limpa dados e calcula indicadores.'''
    df = df.dropna(subset=["valor"])
    df["receita_liquida"] = df["valor"] - df["desconto"].fillna(0)
    return df

def carregar_dados(df, destino):
    '''Salva dados prontos em um arquivo parquet.'''
    df.to_parquet(destino, index=False)

if __name__ == "__main__":
    dados = extrair_dados("dados/vendas_brutas.csv")
    prontos = transformar_dados(dados)
    carregar_dados(prontos, "saidas/vendas_prontas.parquet")
```

## Explicação passo a passo
1. Defina funções separadas para extrair, transformar e carregar.
2. Remova registros inválidos e calcule receita líquida.
3. Utilize formato parquet para armazenar de forma otimizada.
4. Proteja a execução com bloco if __name__ == "__main__".
5. Automatize a execução via agendador externo.

## Resultado esperado
O pipeline lê dados brutos, trata e exporta em formato eficiente, pronto para análises ou dashboards.
