# Automatizar lógica com stored procedure

## Descrição
Ensina a encapsular regras de negócio em uma stored procedure reutilizável.

## Código
```sql
CREATE PROCEDURE sp_registrar_pedido
    @id_cliente INT,
    @id_produto INT,
    @valor DECIMAL(10,2)
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRANSACTION;
    INSERT INTO pedidos (id_cliente, id_produto, valor)
    VALUES (@id_cliente, @id_produto, @valor);
    COMMIT;
END;
```

## Explicação passo a passo
1. Defina parâmetros de entrada conforme necessidade.
2. Inclua lógicas de validação ou transações na procedure.
3. Crie a procedure no banco.
4. Execute usando EXEC sp_registrar_pedido 1, 10, 250.00.
5. Monitore logs para garantir execução correta.

## Resultado esperado
A procedure centraliza regras de inserção de pedidos, evitando repetição de código em aplicações.
