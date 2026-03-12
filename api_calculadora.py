#Não entendi muito bem como que faço uma API, vou precisar estudar com mais calma

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculadora", methods=["POST"])
def calculadora():

    dados = request.get_json()

    num1 = dados.get("numero1")
    num2 = dados.get("numero2")
    operacao = dados.get("operacao")

    if operacao == "soma":
        resultado = num1 + num2

    elif operacao == "subtracao":
        resultado = num1 - num2

    elif operacao == "multiplicacao":
        resultado = num1 * num2

    elif operacao == "divisao":
        if num2 == 0:
            return jsonify({"erro": "Divisão por zero não permitida"})
        resultado = num1 / num2

    else:
        return jsonify({"erro": "Operação inválida"})

    return jsonify({
        "numero1": num1,
        "numero2": num2,
        "operacao": operacao,
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(debug=True)