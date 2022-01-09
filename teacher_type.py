class Teacher_type:
    instances = []

    def __init__(self, type_teacher = None):
        self.__type_teacher = type_teacher
        self.__teachers = []
        self.__class__.instances.append(self)

    @property
    def teachers(self):
        return self.__teachers

    @property
    def type_teacher(self):
        return self.__type_teacher

    @type_teacher.setter
    def type_teacher(self, value):
        self.__type_teacher =  value

    @type_teacher.deleter
    def type_teacher(self):
        del self.__type_teacher

    def type_define(self, teacher):
        if teacher in self.__teachers:
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name} con id: \"{teacher.id_teacher}\" ya esta establecido como profesor de tipo \"{self.__type_teacher}\".")       
            return False 
        else:
            teacher.teacher_type = self
            self.__teachers.append(teacher)
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name} con id: \"{teacher.id_teacher}\" fue establecido exitosamente como profesor de tipo \"{self.__type_teacher}\".")       
            return True     

    def __str__(self):
        return "Tipo de Profesor"