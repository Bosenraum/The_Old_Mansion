
from entity.entity import Entity


class Player(Entity):

    def __init__(self, name, spot):
        super().__init__(name)
        self.__location = None
        self.location = spot

    def move(self, spot):
        self.location = spot

    # Make this a property with a private variable so we can do validation
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, spot):
        self.__location = spot
