# Paralelizar tarefas com multiprocessing

## Descrição
Mostra como acelerar processamento pesado dividindo trabalho em múltiplos processos.

## Código
```python
from multiprocessing import Pool

def calcular_soma(n):
    return sum(range(n))

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        resultados = pool.map(calcular_soma, [10_000_000, 12_000_000, 8_000_000, 15_000_000])
    print(resultados)
```

## Explicação passo a passo
1. Importe Pool de multiprocessing.
2. Defina função intensiva que será executada em paralelo.
3. Crie pool com número adequado de processos.
4. Use map para distribuir lista de tarefas.
5. Execute o script verificando ganho de tempo em relação à execução sequencial.

## Resultado esperado
As somas são calculadas em paralelo, reduzindo o tempo total de processamento.
