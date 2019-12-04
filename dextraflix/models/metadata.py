from marshmallow import Schema, fields, pprint


class MetadataSchema(Schema):
    """
    Metadata scheme
    """
    name = fields.Str()
    value = fields.Str()

metadata_schema = MetadataSchema()
metadatas_schema = MetadataSchema(many=True)