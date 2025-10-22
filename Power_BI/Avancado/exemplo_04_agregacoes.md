# Criar tabelas de agregação para desempenho

## Descrição
Crie tabelas agregadas que aceleram consultas mantendo detalhes disponíveis sob demanda.

## Código
```dax
TabelaAgregada =
SUMMARIZECOLUMNS(
    DimProduto[Categoria],
    DimCalendario[Ano],
    "Receita", SUM(FatoVendas[Receita])
)
```

## Explicação passo a passo
1. Crie uma nova tabela agregada no DAX resumindo dados por categoria e ano.
2. Marque a tabela como Agregação no menu Modelagem.
3. Mapeie os campos agregados para a tabela fato.
4. Defina a agregação como Sum e contagem adequada.
5. Teste a performance analisando o tempo de resposta dos visuais.

## Resultado esperado
Consultas que usam campos agregados são respondidas pela tabela resumida, reduzindo tempo de carregamento.
