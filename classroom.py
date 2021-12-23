class Classroom:
    instances = []

    def __init__(self, classroom_name = None, floor_number = 0, seats_capacity = None):
        self.__classroom_name = classroom_name
        self.__floor_number = floor_number
        self.__building_number = None
        self.__courses = []
        self.__seats_capacity = seats_capacity
        self.__class__.instances.append(self)

    @property
    def classroom_name(self):
        return self.__classroom_name

    @classroom_name.setter
    def classroom_name(self, value):
        self.__classroom_name = value

    @classroom_name.deleter
    def classroom_name(self):
        del self.__classroom_name

    @property
    def floor_number(self):
        return self.__floor_number

    @floor_number.setter
    def floor_number(self, value):
        self.__floor_number = value

    @floor_number.deleter
    def floor_number(self):
        del self.__floor_number

    @property
    def building_number(self):
        return self.__building_number

    @building_number.setter
    def building_number(self, value):
        self.__building_number = value

    @building_number.deleter
    def building_number(self):
        del self.__building_number

    @property
    def seats_capacity(self):
        return self.__seats_capacity

    @seats_capacity.setter
    def seats_capacity(self, value):
        self.__seats_capacity = value

    @seats_capacity.deleter
    def seats_capacity(self):
        del self.__seats_capacity

    def add_course(self, course):
        if self.__building_number == None:
            return print("Antes de agregar un curso al aula, debe agregar el aula a un edificio.")
        
        
        if self.__seats_capacity == None:
            return print("No ha indicado la cantidad de asientos que tiene el aula.")
        elif course.max_students == 0:
            return print("No ha indicado la cantidad máxima de alumnos que tendra el curso.")
        elif course.max_students <= self.__seats_capacity:
            if course in self.__courses:
                return print("El curso {} ya esta vinculado al aula {}.".format(course.course_name, self.__classroom_name))
            else:
                self.__courses.append(course)
                return print("Curso {} agregado exitosamente al aula {}.".format(course.course_name, self.__classroom_name))
        elif course.max_students > self.__seats_capacity:
            return print("La cantidad máxima de alumnos que tendra el curso {}, excede la capacidad de asientos del aula {}".format(course.course_name, self.__classroom_name))

    def __str__(self):
        return "Aula"

        