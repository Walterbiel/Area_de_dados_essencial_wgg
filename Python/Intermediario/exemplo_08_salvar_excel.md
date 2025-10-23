# Exportar resultados para Excel

## Descrição
Ensina a salvar DataFrames em planilhas Excel com várias abas.

## Código
```python
with pd.ExcelWriter("relatorio_vendas.xlsx") as writer:
    vendas.to_excel(writer, sheet_name="Base", index=False)
    receita_categoria.reset_index().to_excel(writer, sheet_name="Resumo", index=False)
```

## Explicação passo a passo
1. Crie um ExcelWriter apontando para o arquivo de saída.
2. Exporte a base completa na aba Base.
3. Salve o resumo por categoria na aba Resumo.
4. Feche o writer utilizando o contexto with.
5. Abra o arquivo para conferir as abas geradas.

## Resultado esperado
Um arquivo Excel é criado com abas organizadas, facilitando o compartilhamento dos resultados.
