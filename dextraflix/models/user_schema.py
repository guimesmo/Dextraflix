from marshmallow import Schema, fields, pprint, post_load
from dextraflix.models.metadata import MetadataSchema

class UserSchema(Schema):
    """
    User model.

    This might be used with User class. If there is no need to have instances
    of Users in this application, then only dictionaries might be used.
    """
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    description = fields.Str(required=True)
    picture = fields.Url(required=True)
    favorites = fields.List(fields.Url(), required=True)
    social_media = fields.List(fields.Url(), required=True)
    metadata = fields.List(fields.Nested(MetadataSchema), required=True)
    is_admin = fields.Bool(required=True)
    
# "Global" instances for schemas
# These objects don't have any states. It is save to declare them here and use
# elsewhere.
user_schema = UserSchema()
users_schema = UserSchema(many=True)
