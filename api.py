from flask import Flask, jsonify

Url = "http://127.0.0.1:5000/ola"

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route("/ola", methods=["GET"])
def Responderola():
    Dados = {"Mensagem":"Hello world"}
    Resposta = jsonify(Dados)
    return Resposta

@app.route("/aluno", methods=["GET"])
def Aluno():
    
    alunos = {12:"Tassio"}
    Resposta = jsonify(alunos)
    return Resposta

