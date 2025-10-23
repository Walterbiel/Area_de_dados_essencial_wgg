# Construir função LAMBDA reutilizável

## Descrição
Crie uma função personalizada no Excel 365 para padronizar códigos de produto com zeros à esquerda.

## Código
```excel
=LAMBDA(codigo;TEXTO(codigo;"00000"))
```

## Explicação passo a passo
1. No Gerenciador de Nomes, crie um novo nome chamado PADRONIZA_ID.
2. Defina a fórmula LAMBDA como mostrado.
3. Nas células da coluna IdProduto, utilize =PADRONIZA_ID(A2).
4. Copie a fórmula para as demais linhas.
5. Combine com validação de dados para garantir consistência.

## Resultado esperado
Todos os códigos são exibidos com cinco dígitos, mantendo o padrão exigido por sistemas externos.
