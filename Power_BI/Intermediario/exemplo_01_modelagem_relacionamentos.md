# Criar relacionamentos entre tabelas

## Descrição
Aprenda a modelar dados conectando tabelas fato e dimensão para análises consistentes.

## Código
```text
# Relacionamentos
# FatoVendas[IdProduto] -> DimProduto[IdProduto]
# FatoVendas[IdCliente] -> DimCliente[IdCliente]
```

## Explicação passo a passo
1. Acesse a exibição Modelo.
2. Arraste o campo IdProduto da FatoVendas para DimProduto.
3. Repita com IdCliente.
4. Verifique se os relacionamentos são 1:* com filtragem cruzada simples.
5. Salve o modelo e volte à tela de relatório.

## Resultado esperado
O modelo relacional garante que medidas agregadas se comportem corretamente entre dimensões.
