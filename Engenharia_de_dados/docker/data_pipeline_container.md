# Docker Data Pipeline Container

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY pipeline.py ./
CMD ["python", "pipeline.py"]
```

O ficheiro acima demonstra uma imagem mínima para executar pipelines de dados. Ele instala dependências e executa um script Python responsável pela ingestão.
