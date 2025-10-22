# Projetar modelo estrela completo

## Descrição
Mostra boas práticas de modelagem estrela com tabelas fato e dimensões otimizadas para Power BI.

## Código
```text
# Estrutura recomendada
# FatoVendas
# DimCliente, DimProduto, DimCalendario, DimCanal
```

## Explicação passo a passo
1. Mapeie os campos de fatos (medidas numéricas) e dimensões (atributos).
2. Separe os dados em tabelas distintas antes de importar.
3. Crie relacionamentos 1:* do lado das dimensões para a fato.
4. Certifique-se de que as dimensões não se relacionem entre si para evitar loops.
5. Documente o modelo para manutenção futura.

## Resultado esperado
O relatório passa a ter um modelo eficiente, permitindo medidas rápidas e filtros consistentes.
