# Particionar tabela de fatos por data

## Descrição
Mostra como dividir grandes volumes em partições mensais para acelerar consultas.

## Código
```sql
CREATE TABLE fatos_vendas (
    id_pedido INT,
    data_venda DATE,
    valor NUMERIC
) PARTITION BY RANGE (data_venda) (
    PARTITION p2023m1 VALUES LESS THAN ('2023-02-01'),
    PARTITION p2023m2 VALUES LESS THAN ('2023-03-01'),
    PARTITION pmax VALUES LESS THAN (MAXVALUE)
);
```

## Explicação passo a passo
1. Planeje o intervalo de partição com base no volume de dados.
2. Crie a tabela definindo PARTITION BY RANGE.
3. Especifique limites para cada partição mensal.
4. Carregue dados e valide em qual partição cada linha foi inserida.
5. Monitore tamanho e desempenho de cada partição.

## Resultado esperado
Consultas filtradas por data percorrem apenas partições relevantes, reduzindo tempo de resposta.
