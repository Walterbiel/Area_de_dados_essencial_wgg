# Controlar operações com TRANSACTION

## Descrição
Mostra como garantir integridade ao inserir múltiplos registros relacionados.

## Código
```sql
BEGIN TRANSACTION;
INSERT INTO pedidos (id_cliente, id_produto, valor) VALUES (1, 10, 250);
INSERT INTO pagamentos (id_pedido, forma_pagamento, valor) VALUES (SCOPE_IDENTITY(), 'Cartão', 250);
COMMIT;
```

## Explicação passo a passo
1. Inicie a transação com BEGIN TRANSACTION.
2. Execute as instruções de inserção relacionadas.
3. Use COMMIT para confirmar as alterações ao final.
4. Substitua por ROLLBACK em caso de erro para desfazer operações.
5. Teste cenários de falha para garantir consistência.

## Resultado esperado
Os registros são inseridos de forma atômica; se ocorrer erro, toda a operação pode ser revertida.
