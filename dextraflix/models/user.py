from .base_model import BaseModel

class User(BaseModel):
    """
    User data class.

    This can be used with UserSchema class in order to create User instaces
    with validated data.

    """
    def __init__(self, **kwargs):
        self.acceptable_attrs = [
            "name",
            "email",
            "description",
            "picture",
            "favorites",
            "social_media",
            "metadata",
            "is_admin"
        ]
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)
