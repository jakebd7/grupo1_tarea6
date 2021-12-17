class Teacher_type:
    instances = []

    def __init__(self, type_teacher = None):
        self.__type_teacher = type_teacher
        self.__class__.instances.append(self)

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
        teacher.teacher_type = self.__type_teacher