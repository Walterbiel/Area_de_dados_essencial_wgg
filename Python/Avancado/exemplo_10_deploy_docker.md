# Empacotar aplicação em contêiner Docker

## Descrição
Ensina a criar Dockerfile para empacotar API e dependências.

## Código
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

## Explicação passo a passo
1. Defina imagem base enxuta do Python.
2. Copie arquivo requirements.txt e instale dependências.
3. Copie código-fonte para o contêiner.
4. Configure comando final usando gunicorn para produção.
5. Construa imagem com `docker build -t api-vendas .` e execute com `docker run -p 8000:8000 api-vendas`.

## Resultado esperado
A aplicação Flask é empacotada em contêiner, pronta para ser executada em qualquer ambiente compatível.
