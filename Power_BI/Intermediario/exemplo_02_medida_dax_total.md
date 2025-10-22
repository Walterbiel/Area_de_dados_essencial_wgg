# Criar medida DAX para total de lucro

## Descrição
Mostra como escrever uma medida reutilizável para calcular o total de lucro.

## Código
```dax
Total Lucro := SUM(FatoVendas[Lucro])
```

## Explicação passo a passo
1. Na tabela FatoVendas, clique em Nova Medida.
2. Digite a fórmula DAX fornecida.
3. Formate o resultado como moeda.
4. Use a medida em gráficos e cartões.
5. Salve o relatório com a medida criada.

## Resultado esperado
A medida Total Lucro fica disponível em todo o modelo, evitando duplicação de cálculos.
