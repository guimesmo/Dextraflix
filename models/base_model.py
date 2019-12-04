
class BaseModel():
    """
    Base model class.

    This class will automatically add attributes based on acceptable_attrs
    list. This must be defined in child classes.
    """

    acceptable_attrs = [ ]
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            if k in self.acceptable_attrs:
                self.__setattr__(k, kwargs[k])
