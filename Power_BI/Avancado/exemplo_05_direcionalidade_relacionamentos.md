# Controlar direcionalidade de relacionamentos

## Descrição
Explica quando usar filtragem cruzada bidirecional para cenários complexos.

## Código
```text
# Configuração
# Relacionamento DimCanal -> FatoVendas: Bidirecional
# Uso controlado em medidas específicas
```

## Explicação passo a passo
1. Identifique cenário em que duas tabelas dimensão precisam se filtrar mutuamente.
2. Acesse a configuração do relacionamento e altere para bidirecional.
3. Teste as medidas afetadas para garantir resultados corretos.
4. Use a função CROSSFILTER em medidas para controlar direcionalidade quando necessário.
5. Documente a decisão para a equipe.

## Resultado esperado
O modelo passa a suportar cenários complexos sem gerar filtros inesperados.
