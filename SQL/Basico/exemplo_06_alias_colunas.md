# Usar alias para renomear colunas

## Descrição
Aprenda a renomear colunas no resultado para melhorar a leitura.

## Código
```sql
-- Renomeia colunas no resultado
SELECT nome AS nome_cliente,
       cidade AS cidade_cliente
FROM clientes;
```

## Explicação passo a passo
1. Escreva a consulta com as colunas desejadas.
2. Use AS para definir um alias amigável.
3. Execute a consulta e confira os novos títulos.
4. Aplique alias para cálculos também.
5. Documente alias usados para consistência.

## Resultado esperado
As colunas aparecem com nomes amigáveis no resultado, facilitando relatórios.
