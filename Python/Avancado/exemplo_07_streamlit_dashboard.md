# Criar dashboard interativo com Streamlit

## Descrição
Apresenta uma aplicação Streamlit simples para explorar métricas de vendas.

## Código
```python
import streamlit as st
import pandas as pd

st.title("Painel de Vendas")
dados = pd.read_csv("dados/vendas.csv")
regiao = st.selectbox("Escolha a região", sorted(dados["regiao"].unique()))
filtrado = dados[dados["regiao"] == regiao]
st.metric("Receita", f"R$ {filtrado['valor'].sum():.2f}")
st.bar_chart(filtrado.groupby("categoria")["valor"].sum())
```

## Explicação passo a passo
1. Instale streamlit (pip install streamlit).
2. Crie interface com st.title e widgets de seleção.
3. Filtre os dados conforme escolha do usuário.
4. Apresente métricas e gráficos interativos.
5. Execute com `streamlit run arquivo.py` e teste no navegador.

## Resultado esperado
O dashboard permite analisar receita por região e categoria de maneira interativa.
