# Combinar ÍNDICE e CORRESP para buscas flexíveis

## Descrição
Demonstra como substituir PROCX com a combinação ÍNDICE + CORRESP quando o PROCX não estiver disponível.

## Código
```excel
=ÍNDICE(TabelaPrecos[Preco];CORRESP(A2;TabelaPrecos[Produto];0))
```

## Explicação passo a passo
1. Garanta que os dados estejam em uma Tabela estruturada.
2. Na célula de destino, insira a fórmula ÍNDICE + CORRESP.
3. Confirme o intervalo de procura e a coluna de retorno.
4. Pressione Enter e copie para as demais linhas.
5. Teste substituindo o produto para validar.

## Resultado esperado
A fórmula retorna o preço correto mesmo se colunas forem movidas, oferecendo flexibilidade na planilha.
