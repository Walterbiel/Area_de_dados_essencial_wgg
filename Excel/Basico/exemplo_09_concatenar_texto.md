# Unir textos com a função CONCAT

## Descrição
Mostra como combinar cidade e estado em um único campo formatado.

## Código
```excel
=CONCAT(A2;" - ";B2)  -- Junta cidade e estado com separador
```

## Explicação passo a passo
1. Na coluna A, liste as cidades e na coluna B, os estados.
2. Na coluna C, insira a fórmula =CONCAT(A2;" - ";B2).
3. Arraste a alça de preenchimento para copiar a fórmula.
4. Aplique alinhamento centralizado se desejar.
5. Use o resultado em relatórios ou tabelas dinâmicas.

## Resultado esperado
Cada linha passa a exibir 'Cidade - Estado', pronto para ser utilizado em relatórios.
