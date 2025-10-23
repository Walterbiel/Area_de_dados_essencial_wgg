# Expor modelo via API Flask

## Descrição
Mostra como disponibilizar um endpoint que recebe dados e retorna previsão.

## Código
```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
modelo = joblib.load("modelos/regressao.joblib")

@app.route("/prever", methods=["POST"])
def prever():
    payload = request.get_json()
    features = [[payload["investimento"], payload["clientes"]]]
    resultado = modelo.predict(features)[0]
    return jsonify({"previsao": resultado})

if __name__ == "__main__":
    app.run(debug=True)
```

## Explicação passo a passo
1. Crie aplicação Flask e carregue modelo treinado.
2. Defina rota POST que recebe JSON.
3. Monte lista de features com os valores recebidos.
4. Retorne previsão em formato JSON.
5. Teste com ferramentas como curl ou Postman.

## Resultado esperado
O endpoint /prever retorna previsão baseada nos dados enviados, permitindo integração com outros sistemas.
