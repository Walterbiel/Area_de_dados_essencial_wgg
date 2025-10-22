# Agendar execução com schedule

## Descrição
Ensina a configurar uma tarefa que roda diariamente para atualizar relatórios.

## Código
```python
import schedule
import time

def atualizar_relatorio():
    print("Atualizando relatório...")
    # Chame funções de leitura, transformação e envio de e-mails aqui

schedule.every().day.at("08:00").do(atualizar_relatorio)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Explicação passo a passo
1. Instale a biblioteca schedule.
2. Defina uma função com as tarefas de atualização.
3. Programe a execução diária com schedule.every().day.at().
4. Mantenha um loop infinito para verificar pendências.
5. Execute o script em ambiente que fique ativo (servidor ou máquina dedicada).

## Resultado esperado
O script executa automaticamente no horário programado, garantindo rotinas consistentes.
