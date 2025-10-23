# Tratar valores ausentes

## Descrição
Ensina a preencher valores nulos com médias ou remover linhas incompletas.

## Código
```python
vendas["desconto"].fillna(0, inplace=True)
vendas_sem_nulos = vendas.dropna()
```

## Explicação passo a passo
1. Identifique colunas com valores ausentes usando isna().sum().
2. Escolha preencher com fillna ou remover com dropna.
3. Aplique inplace=True para atualizar o DataFrame original.
4. Confirme que não existem mais valores nulos.
5. Documente decisões para manter rastreabilidade.

## Resultado esperado
Os dados ficam completos e prontos para análises sem interrupções causadas por valores ausentes.
