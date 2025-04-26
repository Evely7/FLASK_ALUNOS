from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',  
    'database': 'cadastro'  
}

# endereço para cadastrar aluno
@app.route('/aluno', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    nome = data['nome']
    email = data['email']
    matricula = data['matricula']
    senha = data['senha']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aluno (matricula, nome, email, senha) VALUES (%s, %s, %s, %s)",
                   (matricula, nome, email, senha))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'})

# endereço para listar os alunos cadastrados
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(alunos)

if __name__ == '__main__':
    app.run(debug=True)
