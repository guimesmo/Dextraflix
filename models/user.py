from marshmallow import Schema, fields, pprint, post_load
from .metadata import MetadataSchema

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
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class User:
    """
    User data class.

    This can be used with UserSchema class in order to create User instaces
    with validated data.

    """
    def __init__(self,
            name,
            email,
            description,
            picture,
            favorites,
            social_media,
            metadata,
            is_admin):
        self.name = name
        self.email = email
        self.description = description
        self.picture = picture
        self.favorites = favorites
        self.social_media = social_media
        self.metadata = metadata
        self.is_admin = is_admin

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)