# 📊 Análise de Dados & Business Intelligence

Esta secção apresenta exemplos práticos que demonstram como estruturar dados e calcular métricas essenciais para apoiar decisões de negócio.

---

## 📂 Conteúdos Disponíveis

### 1. **Modelagem_de_bancodedados**
- `sales_star_schema.sql` define um **Star Schema** completo para uma fact table de vendas e dimensões de data, cliente e produto.
- Inclui `vw_revenue_by_category`, uma view de agregação já otimizada para dashboards.

### 2. **Python_para_analise**
- `kpi_analysis.py` oferece funções para cálculo de **receita por segmento**, **ticket médio** e **taxa de crescimento** usando `SaleRecord` como estrutura de dados tipada.

### 3. **SQL**
- `retail_queries.sql` contém consultas testadas para receita por categoria e ticket médio por segmento, prontas para uso em ferramentas de BI.

### 4. **Tipos_de_analises_e_metricas**
- `analytics_playbook.py` organiza definições dos tipos de análise (descritiva, diagnóstica, preditiva e prescritiva) e fornece utilitários para filtrar métricas e gerar descrições amigáveis para dashboards.

---

## ✅ Como validar
Todos os scripts possuem testes automatizados com `pytest`, garantindo que o schema SQL é criado corretamente e que os cálculos de KPI devolvem os valores esperados.
