import pru

class Pru:
    instances = []

    def __init__(self, name):
        self.__name = name
        self.__class__.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

def check(obj):
    #del obj
    #print(f"antes de eliminar: {pru.juan.name}")
    del pru.juan