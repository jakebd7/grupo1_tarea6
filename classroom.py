class Classroom:
    instances = []

    def __init__(self, classroom_name = None, floor_number = 0, seats_capacity = None):
        self.__classroom_name = classroom_name
        self.__floor_number = floor_number
        self.__building_number = "No Establecido"
        self.__courses = []
        self.__seats_capacity = seats_capacity
        self.__class__.instances.append(self)

    @property
    def courses(self):
        return self.__courses

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
        if value < 0:
            print("\nEl número de piso del aula debe ser un número entero positivo mayor o igual a 0.")
        else:         
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
        if value < 0:
            print("\nLa capacidad de asientos del aula debe ser un número entero positivo mayor o igual a 0.")
        else:     
            self.__seats_capacity = value

    @seats_capacity.deleter
    def seats_capacity(self):
        del self.__seats_capacity

    def add_course(self, course):
        if self.__building_number == "No Establecido":
            print("\nAntes de agregar un curso al aula, debe agregar el aula a un edificio.")
            return False 
        
        
        if self.__seats_capacity == None:
            print("\nNo ha indicado la cantidad de asientos que tiene el aula.")
            return False
        elif course.max_students == 0:
            print("\nNo ha indicado la cantidad máxima de alumnos que tendra el curso.")
            return False
        elif course.max_students <= self.__seats_capacity:
            if course in self.__courses:
                print(f"\nEl curso \"{course.course_name}\" ya esta vinculado al aula \"{self.__classroom_name}\".")
                return False
            else:
                self.__courses.append(course)
                print(f"\nCurso \"{course.course_name}\" agregado exitosamente al aula \"{self.__classroom_name}\".")
                return True
        elif course.max_students > self.__seats_capacity:
            print(f"\nLa cantidad máxima de alumnos que tendra el curso \"{course.course_name}\", excede la capacidad de asientos del aula \"{self.__classroom_name}\".")
            return False

    def __str__(self):
        return "Aula"

        