# Incorporar script Python em visual do Power BI

## Descrição
Utilize Python para criar gráficos personalizados, como boxplots, dentro do Power BI.

## Código
```python
import pandas as pd
import matplotlib.pyplot as plt

# dataset é fornecido automaticamente
plt.figure(figsize=(6,4))
plt.boxplot(dataset['Receita'])
plt.title('Distribuição de Receita por Cliente')
plt.show()
```

## Explicação passo a passo
1. Habilite suporte a scripts Python no Power BI Desktop.
2. Insira um visual Python e arraste os campos necessários.
3. Cole o script fornecido no editor.
4. Execute o visual e ajuste formatação.
5. Garanta que a máquina cliente possua bibliotecas necessárias.

## Resultado esperado
O relatório exibe um boxplot gerado por Python, enriquecendo as análises com visualizações avançadas.
