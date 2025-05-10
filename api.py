from flask import Flask, request, jsonify

app = Flask(__name__)

estado_porta = "fechada"  # Estado inicial
erro_esp = None           # Último erro do ESP

@app.route('/comando', methods=['GET', 'POST'])
def comando():
    global estado_porta, erro_esp
    if request.method == 'POST':
        data = request.json
        comando = data.get('comando')
        if comando in ['abrir', 'fechar']:
            estado_porta = comando
            erro_esp = None
            return jsonify({"status": "comando recebido"})
        return jsonify({"erro": "comando inválido"}), 400
    else:
        return jsonify({"estado": estado_porta})

@app.route('/erro', methods=['POST'])
def registrar_erro():
    global erro_esp
    data = request.json
    erro_esp = data.get('erro')
    return jsonify({"status": "erro registrado"})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"erro": erro_esp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
