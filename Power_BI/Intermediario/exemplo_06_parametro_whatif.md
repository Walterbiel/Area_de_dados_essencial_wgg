# Criar parâmetro What-If para meta de crescimento

## Descrição
Mostra como adicionar um parâmetro que simula diferentes metas de crescimento anual.

## Código
```text
# Parâmetro criado em Modelagem > Novo Parâmetro
# Intervalo: 0% a 30%, passo 1%
# Medida: Meta Crescimento Valor
```

## Explicação passo a passo
1. Acesse Modelagem > Novo Parâmetro > What if.
2. Configure intervalo de 0 a 0,3 com incremento de 0,01.
3. Insira o slicer gerado no relatório.
4. Crie medida Receita Projetada = SUM(FatoVendas[Receita]) * (1 + 'Meta Crescimento Valor').
5. Compare receita atual e projetada em um gráfico.

## Resultado esperado
Usuários simulam metas de crescimento e visualizam impacto nas receitas diretamente no relatório.
