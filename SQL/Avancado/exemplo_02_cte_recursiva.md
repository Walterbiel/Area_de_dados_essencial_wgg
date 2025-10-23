# Construir CTE recursiva para hierarquias

## Descrição
Mostra como percorrer hierarquia de cargos utilizando Common Table Expression recursiva.

## Código
```sql
WITH RECURSIVE hierarquia AS (
    SELECT id_funcionario, nome, id_gerente, 1 AS nivel
    FROM funcionarios
    WHERE id_gerente IS NULL
    UNION ALL
    SELECT f.id_funcionario, f.nome, f.id_gerente, h.nivel + 1
    FROM funcionarios f
    JOIN hierarquia h ON h.id_funcionario = f.id_gerente
)
SELECT * FROM hierarquia;
```

## Explicação passo a passo
1. Defina a parte âncora com os gestores principais.
2. Use UNION ALL para adicionar linhas filhos na parte recursiva.
3. Incrementa o nível a cada iteração.
4. Execute a consulta para listar toda a hierarquia.
5. Ordene por nível para facilitar leitura.

## Resultado esperado
A CTE retorna todos os colaboradores com seus níveis hierárquicos, facilitando análises organizacionais.
