# Aplicar funções com apply

## Descrição
Mostra como criar uma coluna de classificação usando função personalizada.

## Código
```python
def classificar_ticket(valor):
    if valor < 100:
        return "Baixo"
    if valor < 500:
        return "Médio"
    return "Alto"

vendas["faixa_ticket"] = vendas["valor"].apply(classificar_ticket)
```

## Explicação passo a passo
1. Defina uma função que receba o valor e retorne a faixa desejada.
2. Aplique apply na coluna valor.
3. Crie uma nova coluna com o resultado.
4. Conte quantas vendas existem em cada faixa usando value_counts().
5. Utilize a coluna em dashboards ou relatórios.

## Resultado esperado
Cada venda recebe uma classificação de ticket, facilitando segmentações.
