# Registrar logs em pipelines

## Descrição
Ensina a usar o módulo logging para acompanhar o andamento de um ETL.

## Código
```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Iniciando extração")
# Coloque aqui a chamada de extração
logging.info("Extração concluída")
```

## Explicação passo a passo
1. Configure logging.basicConfig com nível INFO.
2. Inclua mensagens antes e depois de cada etapa do pipeline.
3. Redirecione logs para arquivo usando parâmetro filename se necessário.
4. Utilize níveis WARNING e ERROR para alertas e falhas.
5. Analise os logs para depurar problemas rapidamente.

## Resultado esperado
As mensagens de log registram cada etapa do ETL, facilitando monitoramento e diagnóstico.
