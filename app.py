from flask import Flask, jsonify, request
import json

desenvolvedores = [
    {"nome": "Marcos",
     "habilidades": ["Django", "Flask"]
     },
    {"nome": "Mario",
     "Habilidades": ["C", "C++"]}
]

app = Flask(__name__)

# devolve um desenvolvedor pelo ID, Alterar e Deleta um desenvolvedor
@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            desenv = desenvolvedores[id]
        except IndexError:
            mensagem = 'Id {} não encontrado'.format(id)
            desenv = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            desenv = {'statua': 'erro', 'mensagem': mensagem}
        return jsonify(desenv)
        # Imprime no terminal
        # print(desenv)
        # return jsonify(desenv)
    elif request.method == "PUT":
        # pega requisição transforma em json
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        # retorna o que foi alterado
        return jsonify(dados)
    elif request.method == "DELETE":
        try:
            desenvolvedores.pop(id)
        except IndexError:
            mensagem = 'Id {} não encontrado'.format(id)
            return jsonify({"status": "Erro", "Mensagem": mensagem})
        return jsonify({"status": "sucesso", "mensagem": "Registro excluído"})

# Listar todos desenvolvedores e Inclui desenvolvedpr
@app.route("/dev/", methods = ["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"status": "sucesso", "mensagem": "Registro incluido"})


if __name__ == '__main__':
    app.run(debug=True)

# POSTMAN
# GET    http://127.0.0.1:5000/dev/1
# RETORNA
# {
#     "Habilidades": [
#         "C",
#         "C++"
#     ],
#     "nome": "Mario"
# }
#
# GET   http://127.0.0.1:5000/dev/0
# {
#     "habilidades": [
#         "Django",
#         "Flask"
#     ],
#     "nome": "Marcos"
# }

# DELETE   http://127.0.0.1:5000/dev/1/
# RETORNA
# {
#     "Mensagem": "Excluído com sucesso",
#     "status": "Sucesso"
# }

# APÓS EXCLUSÃO
# GET      http://127.0.0.1:5000/dev/1
# RETORNA
# {
#     "mensagem": "Id 1 não encontrado",
#     "status": "erro"
# }

# POST     http://127.0.0.1:5000/dev/   body raw JSON
# ENTRADA
# "Habilidades": [
#         "DBASE",
#         "CLIPPER"
#     ],
#     "Nome": "SANDRO"
# }
# SAÍDA
# {
#     "mensagem": "Registro incluido",
#     "status": "sucesso"
# }

# # GET    http://127.0.0.1:5000/dev/   body raw JSON
# RETORNA
# {
#     "Habilidades": [
#         "DBASE",
#         "CLIPPER"
#     ],
#     "Nome": "SANDRO"
# }