# Buscar informações com XLOOKUP (PROCX)

## Descrição
Demonstra o uso do PROCX para trazer automaticamente o preço de um produto a partir de outra tabela.

## Código
```excel
=PROCX(A2;TabelaPrecos[Produto];TabelaPrecos[Preco];"Produto não encontrado")
```

## Explicação passo a passo
1. Garanta que há duas tabelas: Pedidos e TabelaPrecos.
2. Na tabela Pedidos, selecione a coluna de preço a preencher.
3. Digite a fórmula PROCX como no exemplo.
4. Arraste para preencher todos os produtos.
5. Trate possíveis erros exibindo mensagem personalizada.

## Resultado esperado
Cada linha de pedido recebe automaticamente o preço correto do produto consultado na tabela de referência.
