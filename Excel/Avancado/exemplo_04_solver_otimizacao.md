# Otimizar mix de produtos com Solver

## Descrição
Use o suplemento Solver para definir a combinação ideal de produtos respeitando restrições de estoque e meta de lucro.

## Código
```text
# Configuração do Solver
# Objetivo: Maximizar célula G2 (lucro total)
# Variáveis de decisão: C2:E2 (quantidades)
# Restrições: C2:E2 >= 0, C2:E2 <= Estoque, G2 >= Meta
```

## Explicação passo a passo
1. Prepare uma planilha com quantidade a produzir, lucro unitário e estoque disponível.
2. Calcule o lucro total multiplicando quantidades por lucro unitário.
3. Acesse Dados > Solver e configure objetivo, variáveis e restrições.
4. Escolha o método Simplex LP e clique em Resolver.
5. Analise o relatório de sensibilidade gerado.

## Resultado esperado
O Solver retorna a quantidade ideal de cada produto para atingir ou superar a meta de lucro respeitando os limites de estoque.
