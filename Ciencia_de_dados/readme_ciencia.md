# 🧠 Ciência de Dados

Esta secção reúne implementações enxutas para treinar, avaliar e preparar modelos de Machine Learning com Python puro.

---

## 📂 Conteúdos Disponíveis

### 1. **Machine_Learning**
- `linear_model.py` implementa uma regressão linear multivariada via gradiente descendente, com interface `fit`/`predict` semelhante a bibliotecas populares.

### 2. **Python_para_ciencia**
- `feature_engineering.py` agrupa utilitários de preparação de dados como normalização min-max, divisão treino/teste e codificação de categorias.

### 3. **Series_Temporais**
- `time_series_models.py` inclui funções para previsão com média móvel e cálculo de índices sazonais.

---

## ✅ Como validar
Utilize `pytest` para executar os testes automatizados: eles verificam convergência do modelo de regressão, consistência das transformações de features e cálculos de séries temporais.
