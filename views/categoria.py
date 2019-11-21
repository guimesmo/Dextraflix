from flask import Blueprint, jsonify, request
from flask import abort

categorias_bp = Blueprint('categorias', __name__)


@categorias_bp.route('/categorias/', methods=['GET', 'PUT'])
def lista_categorias():
    from main import mongo
    from models.categoria import Categoria

    if request.method == 'PUT':
        data = request.get_json()
        categoria = Categoria(nome=data.get("nome"),
                              descricao=data.get("descricao"))
        categoria.save()

        return jsonify(categoria.as_dict())

    categorias = mongo.db.categoria.find()
    output = []

    for categoria in categorias:
        categoria = Categoria.from_dict(categoria)
        output.append(categoria.as_dict())

    return jsonify(output)


@categorias_bp.route('/categorias/<nome>', methods=['GET', 'POST', 'DELETE'])
def categoria(nome):
    from main import mongo
    from models.categoria import Categoria
    categoria = mongo.db.categoria.find_one({'nome': nome})
    if not categoria:
        abort(404)

    categoria = Categoria.from_dict(categoria)

    if request.method == 'POST':
        data = request.get_json()
        categoria.nome = data.get('nome')
        categoria.descricao = data.get('descricao')
        categoria.save()

    if request.method == 'DELETE':
        categoria.delete()
        return jsonify({'message': 'ok'})

    return jsonify(categoria.as_dict())



