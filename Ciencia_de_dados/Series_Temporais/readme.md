## Série Temporal 

Uma **série temporal** é um conjunto de dados **organizados em ordem cronológica**.  
- Cada valor está associado a um **momento específico** (dia, mês, ano, hora, etc.).  
- Serve para **analisar padrões** como tendências, sazonalidade ou variações no tempo.  

**Exemplo:**
| Data       | Vendas |
|------------|--------|
| 01/01/2024 | 100    |
| 02/01/2024 | 120    |
| 03/01/2024 | 90     |

Usada em meteorologia, economia, finanças, produção e mais.

-Exemplo gráfico de uma série temporal:

<img width="280" height="180" alt="image" src="https://github.com/user-attachments/assets/6d9ac8eb-6fb2-4730-9e57-17c476817234" />

-------------------------------------------------------------------------------------------

## Componentes de uma Série Temporal:

<img width="300" height="168" alt="image" src="https://github.com/user-attachments/assets/a63962cb-8fcb-45d7-b9fd-85240897710d" />

### Abordagem Técnica
A decomposição clássica assume que a série temporal $Y_t$ pode ser representada como:

- **Modelo aditivo**: $Y_t = T_t + S_t + E_t$
- **Modelo multiplicativo**: $Y_t = T_t \times S_t \times E_t$

Onde:
- $T_t$ = tendência
- $S_t$ = componente sazonal
- $E_t$ = componente aleatório (erro)


## Decomposição da Tendência de uma Série Temporal

A decomposição de uma série temporal é o processo de separar os seus diferentes componentes — **tendência**, **sazonalidade** e **ruído** — para compreender melhor o comportamento dos dados. Um dos principais elementos é a **tendência**.

A **tendência** representa o movimento de longo prazo da série, ou seja, a direção geral dos dados ao longo do tempo, independentemente das flutuações sazonais ou aleatórias.

---
### Cálculo da Tendência
1. **Médias móveis**:
   - Para dados trimestrais, uma média móvel centrada de 4 trimestres:
     $$T_t = \frac{Y_{t-2} + Y_{t-1} + Y_t + Y_{t+1}}{4}$$
   - Este processo suaviza variações sazonais e ruído, revelando o padrão de longo prazo.

2. **Regressão linear**:
   - Ajusta-se um modelo $T_t = a + b t$ via mínimos quadrados.
   - $a$ é o intercepto e $b$ a taxa média de variação por período.

3. **Filtros estatísticos**:
   - Ex.: Filtro de Hodrick–Prescott (HP) para extrair tendências suaves.

---
### Interpretação
Após o cálculo, a tendência pode mostrar:
- **Crescimento** ($b > 0$)
- **Queda** ($b < 0$)
- **Estabilidade** ($b \approx 0$)

> **Exemplo:** Numa série de vendas trimestrais de pacotes turísticos, o uso de médias móveis de 4 trimestres pode evidenciar uma subida constante após 2021, indicando recuperação do setor pós-pandemia.

## Decomposição da Sazonalidade de uma Série Temporal

