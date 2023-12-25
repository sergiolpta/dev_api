from flask import Flask
from flask_restful import Resource, Api, request
import json

app = Flask(__name__)
api = Api(app)
# devolve um desenvolvedor pelo ID, também altera e deleta desenvolvedor
desenvolvedores = [
    {
         'id':'0',
         'nome': 'Sergio',
         'habilidades':['Python', 'Flask']
     },
    {
        'id': '1',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = (f'Desenvolvedor de ID {id} não existe')
            response = {'satus': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'satus': 'erro', 'mensagem': mensagem}
        return (response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'Registro excluido'})
# Lista de todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)