# Conectar ao banco com SQLAlchemy

## Descrição
Ensina a criar engine e ler dados diretamente de um banco relacional.

## Código
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://usuario:senha@localhost:5432/dados")
query = "SELECT * FROM vendas"
vendas_db = pd.read_sql(query, engine)
```

## Explicação passo a passo
1. Instale driver apropriado (psycopg2 para PostgreSQL).
2. Monte string de conexão com credenciais.
3. Crie engine com create_engine.
4. Leia dados com pd.read_sql.
5. Feche conexões reutilizando a engine quando possível.

## Resultado esperado
Os dados são carregados diretamente do banco relacional em um DataFrame pandas.
