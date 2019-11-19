from flask import Blueprint, jsonify, request
from flask import abort

videos_bp = Blueprint('videos', __name__)

@videos_bp.route('/videos/', methods=['GET', 'PUT'])
def lista_videos():
    from Dextraflix.main import mongo
    from Dextraflix.models.video import Video 

    if request.method == 'PUT':
        data = request.get_json()
        video = video(
            nome=data.get("nome"),
            slug=data.get("slug"),
            descricao=data.get("descricao"),
            data=data.get("data"),
            url=data.get("url"),
            categoria_id=data.get("categoria_id"),
            hashtags=data.get("hashtags"),
            metadados=data.get("metadados"),
            autores=data.get("autores"))
        video.save()

        return jsonify(video.as_dict())

    videos = mongo.db.videos.find()
    output = []

    for video in videos:
        video = video.from_dict(video)
        output.append(video.as_dict())

    return jsonify(output)


@videos_bp.route('/videos/<slug>', methods=['GET', 'POST', 'DELETE'])
def video(slug):
    from Dextraflix.main import mongo
    from Dextraflix.models.video import Video
    video = mongo.db.videos.findOne({'slug': slug})
    if not Video:
        abort(404)

    video = video.from_dict(video)

    if request.method == 'POST':
        data = request.get_json()
        video.nome = data.get('nome')
        video.slug = data.get('slug')
        video.descricao = data.get('descricao')
        video.data = data.get('data')
        video.url = data.get('url')
        video.categoria_id = data.get('categoria_id')
        video.hashtags = data.get('hashtags')
        video.metadados = data.get('metadados')
        video.autores = data.get('autores')
        video.save()

    if request.method == 'DELETE':
        video.delete()
        return jsonify({'message': 'ok'})

    return jsonify(video.as_dict())

# CREATE
@videos_bp.route('/videos', methods=['POST'])
def create():
    from Dextraflix.main import mongo
    from Dextraflix.models.video import Video

    if request.method == 'POST':
        data = request.get_json()

        video = Video(
            data.get('nome'),
            data.get('slug'),
            data.get('data'),
            data.get('url'),
            data.get('categoria_id'),
            data.get('descricao'),
            data.get('hashtags'),
            data.get('metadados'),
            data.get('autores')
        )
        
        video.save()

    return jsonify(video.as_dict())
