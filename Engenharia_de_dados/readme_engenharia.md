# 🏗️ Engenharia de Dados

Scripts e modelos desta pasta demonstram como integrar sistemas, padronizar pipelines e validar transformações em diferentes ferramentas do ecossistema de dados.

---

## 📂 Conteúdos Disponíveis

### 1. **API**
- `api_client.py` implementa um cliente para leitura de respostas JSON com validação de schema para leituras meteorológicas.

### 2. **Azure**
- `data_lake.py` fornece a classe `DataLakePath` que padroniza URIs particionadas no Azure Data Lake.

### 3. **CI-CD**
- `pipeline.py` simula a resolução de dependências entre estágios de um pipeline de dados.

### 4. **Kafka**
- `in_memory_kafka.py` representa tópicos Kafka em memória com operações de `produce`/`consume` para prototipagem.

### 5. **Python_para_engenharia**
- `etl_utils.py` inclui funções de deduplicação e enriquecimento de registos para pipelines ETL.

### 6. **SQL_para_engenharia**
- `warehouse_transformations.sql` cria estruturas de staging e uma view de features para churn.

### 7. **airflow**
- `dag_example.py` descreve uma estrutura simples de DAG com verificação de dependências cíclicas.

### 8. **dbt-databuildtool**
- `models/dim_customers.sql` demonstra um modelo dbt com `ref` e limpeza de dados.

### 9. **docker**
- `data_pipeline_container.md` documenta um `Dockerfile` minimalista para executar pipelines Python.

### 10. **spark**
- `spark_like.py` fornece uma API inspirada em DataFrames do Spark para filtragem e seleção em memória.

---

## ✅ Como validar
Os testes com `pytest` verificam o comportamento de cada componente: clientes de API, resolução de DAGs, simulação de Kafka, SQL de warehouse e documentação de Docker.
