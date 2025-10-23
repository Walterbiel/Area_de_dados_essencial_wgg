# Criar view para reutilizar consultas

## Descrição
Demonstra como salvar uma consulta complexa como view para acesso rápido.

## Código
```sql
CREATE VIEW vw_vendas_categoria AS
SELECT pr.categoria,
       SUM(p.valor) AS total_categoria
FROM pedidos p
JOIN produtos pr ON pr.id_produto = p.id_produto
GROUP BY pr.categoria;
```

## Explicação passo a passo
1. Escreva a consulta que será reutilizada frequentemente.
2. Use CREATE VIEW com um nome descritivo.
3. Execute a instrução para criar a view.
4. Consuma os dados usando SELECT * FROM vw_vendas_categoria.
5. Atualize a view caso as regras de negócio mudem.

## Resultado esperado
A view `vw_vendas_categoria` pode ser consultada por diversos relatórios sem reescrever a lógica.
