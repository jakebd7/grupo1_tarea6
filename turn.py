class Turn:
    instances = []

    def __init__(self, turn = None):
        self.__turn = turn
        self.__teachers = []
        self.__class__.instances.append(self)


    @property
    def teachers(self):
        return self.__teachers

    @property
    def turn(self):
        return self.__turn

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
        if teacher in self.__teachers:
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name}\" con id: \"{teacher.id_teacher}\" ya esta agregado al turno \"{self.__turn}\".")       
            return False 
        else:
            teacher.turn = self
            self.__teachers.append(teacher)
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name}\" con id: \"{teacher.id_teacher}\" fue agregado exitosamente al turno \"{self.__turn}\".")       
            return True            

    def __str__(self):
        return "Turno"
    