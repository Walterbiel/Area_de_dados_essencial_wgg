# Configurar atualização incremental

## Descrição
Demonstra como usar políticas de atualização incremental para grandes volumes de dados.

## Código
```text
# Política de atualização incremental
# Faixa histórica: 5 anos
# Faixa incremental: 1 mês
```

## Explicação passo a passo
1. Crie parâmetros RangeStart e RangeEnd no Power Query.
2. Aplique filtro de data usando esses parâmetros na tabela fato.
3. No Power BI Desktop, defina política de atualização incremental para a tabela.
4. Publique o relatório no serviço.
5. Configure a atualização agendada; apenas o último mês será recarregado.

## Resultado esperado
A atualização passa a ser mais rápida, pois somente dados recentes são recarregados.
