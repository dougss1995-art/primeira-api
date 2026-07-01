from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana", "cursa": "Técnico em Informática"},
    {"id": 2, "nome": "Bruno", "cursa": "Técnico em Desenvolvimento"},
    {"id": 3, "nome": "Carla", "cursa": "Técnico em Informática"}
]

tarefas = [
    {
        "id": 1,
        "titular": 'Estudar Flask',
        "Descricao": 'Criar minha Primeira API',
        "concluida": False
    },

    {
        "id": 2,
        "titular": 'Fazer exercicíos',
        "Descricao": 'Praticar endpoints de API',
        "concluida": False
    }
]



@app.route("/")
def home():
    return jsonify({
        "message": "Minha primeira  API está funcionando",
        "status": "ok"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok", "menssagem": "API está funcionando"})



@app.route("/alunos")
def listar_alunos():
    return jsonify(alunos)



@app.route("/alunos/<int:id>")
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)

    return jsonify({"erro": "Aluno não encontrado"}), 404


@app.route('/tarefas')
def lista_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas/<int:id>')
def buscar_tarefas(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            return jsonify(tarefa)

    return jsonify({'erro': 'Tarefa não encontrada'})


@app.route('/tarefas', methods=['POST'])
def criar_tarefas():
    dados = request.get_json()

    if not dados:
        return jsonify({"Erro": "Nenhum dado foi enviado."}), 400

    if not dados:
        return jsonify({"Erro": "Os campos 'titulo' e 'descrição' são obrigatorios."}), 400


    nova_tarefa = {
        "id": len(tarefas)+1,
        "titular": dados["titular"],
        "descricao": dados["descricao"],
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"Erro": "Nenhum dado foi enviado."}), 400

    if not dados:
        return jsonify({"Erro": "Os campos 'nome' e 'cursa' são obrigatorios."}), 400


    novo_aluno = {
        "id": len(alunos)+1,
        "nome": dados["nome"],
        "cursa": dados["cursa"],
        "concluida": False
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()

    campos_obrigatorios = [
        "titular",
        "descricao",
        "concluida"
    ]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório."}), 400

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titular"] = dados["titular"]
            tarefa["descricao"] = dados["descricao"]
            tarefa["concluida"] = dados["concluida"]

            return jsonify(tarefa), 201

    return jsonify({"erro": "Não encontrado"}), 404


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    dados = request.get_json()

    campos_obrigatorios = [
        "nome",
        "cursa"
    ]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório."}), 400


    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = dados["nome"]
            aluno["cursa"] = dados["cursa"]

            return jsonify(aluno), 201

    return jsonify({"erro": "Não encontrado"}), 404

@app.route('/terefas/<int:id>', methods=['PATCH'])
def atualizar_campo_tarefas(id):
    dados_tarefas = request.get_json()

    for tarefa in tarefas:
        if tarefa["id"] == id:
            if "titular" in dados_tarefas["titular"]:
                tarefa["titular"] = dados_tarefas["titular"]

            if "descricao" in dados_tarefas["descricao"]:
                tarefa["descricao"] = dados_tarefas["descricao"]

            if "concluida" in dados_tarefas["concluida"]:
                tarefa["concluida"] = dados_tarefas["concluida"]

            return jsonify(tarefa), 201

    return jsonify({"erro": "ID tarefa não encontrada"}), 404

''' 
 @app.route('/tarefas/<int:id>', methods=['PATCH'])
def atualizar_campo_tarefas(id):
    dados_tarefas = request.get_json()

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titular"] = dados_tarefas.get("titular", tarefa["titular"])
            tarefa["descricao"] = dados_tarefas.get("descricao", tarefa["descricao"])
            tarefa["concluida"] = dados_tarefas.get("concluida", tarefa["concluida"])

            return jsonify(tarefa), 201

    return jsonify({"erro": "ID tarefa não encontrado"}), 404
'''
@app.route('/alunos/<int:id>', methods=['PATCH'])
def atualizar_campo_aluno(id):
    dados_aluno = request.get_json()

    for aluno in alunos:
        if aluno["id"] == id:
            if "nome" in dados_aluno["nome"]:
                aluno["cursa"] = dados_aluno["cursa"]

            if "cursa" in dados_aluno["cursa"]:
                aluno["cursa"] = dados_aluno["cursa"]

            if "concluida" in dados_aluno["concluida"]:
                aluno["concluida"] = dados_aluno["concluida"]

'''
@app.route('/alunos/<int:id>', methods=['DELETE'])
def atualizar_campo_aluno(id):
    dados_aluno = request.get_json()

    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = dados_aluno.get("nome", aluno["nome"])
            aluno["descricao"] = dados_aluno.get("descricao", aluno["descricao"])

            return jsonify(aluno), 201
'''

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)

            return jsonify(tarefa), 200

    return jsonify({"erro": "ID tarefa não encontrada"}), 404


@app.route('/alunos/<int:id>', methods=['DELETE'])
def excluir_aluno(id):

    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)

            return jsonify(aluno), 200

    return jsonify({"erro": "ID aluno não encontrado"})


if __name__ == "__main__":
    app.run(debug=True)