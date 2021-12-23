class Turn:
    instances = []

    def __init__(self, turn = None):
        self.__turn = turn
        self.__teacher = {}
        self.__class__.instances.append(self)

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    @turn.deleter
    def turn(self):
        del self.__turn

    def turn_define(self, teacher):
        teacher.turn = self.__turn

    def __str__(self):
        return "Turno"
    