# Escrever testes com pytest

## Descrição
Demonstra como validar funções de transformação usando asserts.

## Código
```python
import pandas as pd
from pipeline import transformar_dados

def test_transformar_dados_calcula_receita():
    df = pd.DataFrame({"valor": [100], "desconto": [10]})
    resultado = transformar_dados(df)
    assert resultado.loc[0, "receita_liquida"] == 90
```

## Explicação passo a passo
1. Instale pytest e crie arquivo de testes.
2. Monte DataFrame de exemplo com valores conhecidos.
3. Chame a função de transformação.
4. Utilize assert para verificar o cálculo.
5. Execute pytest para garantir que a lógica se mantém correta.

## Resultado esperado
O teste automatizado garante que alterações futuras não quebrem o cálculo de receita líquida.
