from flask import Flask, jsonify,request
import json

app = Flask(__name__)

desenvolvedores = [
    {   'id':'0',
        'nome':'Vinicius',
        'habilidades':['Python','Flask']},
    {   
        'id':'1',
        'nome':'Lima',
        'habilidades':['Python','Django']}
]

# Devolve um desenvolvedor pelo ID. Também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido. Procure o adminstrador da API'
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados 
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro excluido'})
    
# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug='True')