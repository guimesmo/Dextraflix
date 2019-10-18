from main import mongo


class Categoria:
    _id = None

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    @staticmethod
    def from_dict(instance_dict):
        categoria = Categoria(nome=instance_dict['nome'],
                              descricao=instance_dict['descricao'])
        categoria._id = instance_dict['_id']
        return categoria

    def save(self):
        if self._id:
            return self.update()
        return self.create()

    def update(self):
        result = mongo.db.categoria.update_one(
            {"_id": self._id},
            {"$set": {"nome": self.nome,
                      "descricao": self.descricao}})
        return result

    def create(self):
        result = mongo.db.categoria.insert_one(
            {"nome": self.nome, "descricao": self.descricao}
        )
        self._id = result.inserted_id
        return result

    def as_dict(self):
        return {
            "_id": str(self._id),
            "nome": self.nome,
            "descricao": self.descricao
        }
