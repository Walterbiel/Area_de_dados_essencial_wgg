# Criar DAG simples no Apache Airflow

## Descrição
Apresenta uma DAG que agenda tarefas de extração e carregamento diariamente.

## Código
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extrair():
    print("Extraindo dados...")

def carregar():
    print("Carregando dados...")

default_args = {
    "owner": "time_dados",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "dag_vendas",
    default_args=default_args,
    schedule_interval="0 6 * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False
)

tarefa_extrair = PythonOperator(
    task_id="extrair_dados",
    python_callable=extrair,
    dag=dag
)

tarefa_carregar = PythonOperator(
    task_id="carregar_dados",
    python_callable=carregar,
    dag=dag
)

tarefa_extrair >> tarefa_carregar
```

## Explicação passo a passo
1. Configure default_args com informações de proprietário e tentativas.
2. Defina DAG com agendamento diário às 6h.
3. Implemente funções Python para extrair e carregar.
4. Crie operadores PythonOperator apontando para as funções.
5. Estabeleça dependência usando operador >>.

## Resultado esperado
A DAG agenda a execução diária das tarefas de extração e carregamento de vendas.
