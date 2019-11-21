from main import mongo

class Video:
    _id = None

    def __init__(self, nome, slug, data, url, categoria_id, descricao, hashtags, metadados, autores):
        self.nome = nome
        self.slug = slug
        self.data = data
        self.url = url
        self.categoria_id = categoria_id
        self.descricao = descricao
        self.hashtags = hashtags
        self.metadados = metadados
        self.autores = autores

    @staticmethod
    def from_dict(instance_dict):
        video = Video(
            nome=instance_dict['nome'],
            slug=instance_dict['slug'],
            data=instance_dict['data'],
            url=instance_dict['url'],
            categoria_id=instance_dict['categoria_id'],
            descricao=instance_dict['descricao'],
            hashtags=instance_dict['hashtags'],
            metadados=instance_dict['metadados'],
            autores=instance_dict['autores'])
        video._id = instance_dict['_id']
        return video

    def save(self):
        if self._id:
            return self.update()
        return self.create()

    def update(self):
        result = mongo.db.videos.update_one(
            {"_id": self._id},
            {"$set": {
                "nome": self.nome,
                "slug": self.slug,
                "data": self.data,
                "url": self.url,
                "categoria_id": self.categoria_id,
                "descricao": self.descricao,
                "hashtags": self.hashtags,
                "metadados": self.metadados,
                "autores": self.autores}})
        return result

    def create(self):
        result = mongo.db.videos.insert_one(
            {
                "nome": self.nome, 
                "slug": self.slug, 
                "descricao": self.descricao,
                "data": self.data,
                "url": self.url,
                "categoria_id": self.categoria_id,
                "hashtags": self.hashtags,
                "metadados": self.metadados,
                "autores": self.autores
            }
        )
        self._id = result.inserted_id
        return result

    def as_dict(self):
        return {
            "_id": str(self._id),
            "nome": self.nome, 
            "slug": self.slug, 
            "descricao": self.descricao,
            "data": self.data,
            "url": self.url,
            "categoria_id": self.categoria_id,
            "hashtags": self.hashtags,
            "metadados": self.metadados,
            "autores": self.autores
        }

    def delete(self):
        result = mongo.db.videos.delete_one({'_id': self._id})
        return result