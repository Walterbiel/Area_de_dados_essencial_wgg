# Modelar dados no Power Pivot com relacionamentos

## Descrição
Crie um modelo de dados relacionando tabelas de fatos e dimensões para análises avançadas.

## Código
```text
# Relacionamentos no Power Pivot
# FatoVendas[IdProduto] -> DimProduto[IdProduto]
# FatoVendas[IdCliente] -> DimCliente[IdCliente]
```

## Explicação passo a passo
1. Carregue as tabelas FatoVendas, DimProduto e DimCliente para o modelo de dados.
2. Abra a janela do Power Pivot.
3. Na exibição de diagrama, arraste os campos de chave entre as tabelas correspondentes.
4. Defina a direção do relacionamento como um-para-muitos, com filtro cruzado.
5. Salve o modelo para uso em Tabelas Dinâmicas ou Power BI.

## Resultado esperado
O Excel passa a ter um modelo relacional robusto que permite análises multidimensionais.
