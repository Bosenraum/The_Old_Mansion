

class Entity:

    # Create a new entity the given name
    def __init__(self, name):
        self.__name = None
        self.name = name

    # TODO:
    # Will allow entities to move on the map
    def move(self, location):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
