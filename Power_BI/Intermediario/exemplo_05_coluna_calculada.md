# Adicionar coluna calculada de faixa etária

## Descrição
Demonstra como classificar clientes em faixas etárias usando SWITCH.

## Código
```dax
Faixa Etária =
SWITCH(TRUE(),
    DimCliente[Idade] < 25, "Jovem",
    DimCliente[Idade] <= 40, "Adulto",
    DimCliente[Idade] <= 60, "Maduro",
    "Sênior"
)
```

## Explicação passo a passo
1. Na tabela DimCliente, crie uma nova coluna.
2. Cole a expressão DAX com SWITCH(TRUE()).
3. Verifique se as faixas foram atribuídas corretamente.
4. Use a coluna Faixa Etária em segmentações.
5. Atualize o relatório para incluir análises por faixa.

## Resultado esperado
Clientes são classificados por faixa etária, permitindo análises demográficas detalhadas.
