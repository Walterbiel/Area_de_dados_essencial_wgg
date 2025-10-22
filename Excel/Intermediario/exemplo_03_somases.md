# Aplicar SOMASES com múltiplos critérios

## Descrição
Veja como somar valores considerando região e canal de vendas simultaneamente.

## Código
```excel
=SOMASES(TabelaVendas[Valor];TabelaVendas[Região];H2;TabelaVendas[Canal];H3)
```

## Explicação passo a passo
1. Crie duas células de critérios: H2 para Região e H3 para Canal.
2. Informe os valores desejados, como 'Sudeste' e 'Loja'.
3. Na célula de resultado, insira a fórmula SOMASES.
4. Pressione Enter e veja a soma filtrada.
5. Altere os critérios para avaliar diferentes cenários.

## Resultado esperado
O valor total retorna apenas para registros que atendem aos critérios definidos, apoiando decisões específicas.
