# Combinar dados com merge

## Descrição
Mostra como juntar vendas e informações de clientes utilizando chaves comuns.

## Código
```python
clientes = pd.read_csv("dados/clientes.csv")
base_completa = vendas.merge(clientes, on="id_cliente", how="left")
print(base_completa.head())
```

## Explicação passo a passo
1. Carregue a tabela de clientes.
2. Use merge especificando a chave id_cliente.
3. Defina how='left' para manter todas as vendas.
4. Cheque registros sem correspondência com base_completa[clientes['nome'].isna()].
5. Salve a base enriquecida se necessário.

## Resultado esperado
A tabela de vendas passa a conter dados de clientes, permitindo análises mais ricas.
