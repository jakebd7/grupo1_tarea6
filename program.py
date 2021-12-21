import time

class Program:
    instances = []

    def __init__(self, program_name = None):
        self.__program_name = program_name
        self.__creation_date_program = time.strftime("%d/%m/%y")
        self.__program_status = None
        self.__principal = ""
        self.__courses = []
        self.__max_students = 0
        self.__min_students = 0
        self.__max_courses = 0
        self.__min_courses = 0
        self.__program_duration = 0
        self.__class__.instances.append(self)

    @property
    def program_name(self):
        return self.__program_name

    @program_name.setter
    def program_name(self, value):
        self.__program_name = value

    @program_name.deleter
    def name_program(self):
        del self.__name_program

    @property
    def creation_date_program(self):
        return self.__creation_date_program

    @creation_date_program.setter
    def creation_date_program(self, value):
        self.__creation_date_program = value

    @creation_date_program.deleter
    def creation_date_program(self):
        del self.__creation_date_program

    @property
    def program_status(self):
        return self.__program_status

    @program_status.setter
    def program_status(self, value):
        self.__program_status = value
    
    @program_status.deleter
    def program_status(self):
        del self.program_status

    @property
    def principal(self):
        return self.__principal

    @principal.setter
    def principal(self, value):
        self.__principal = value

    @principal.deleter
    def principal(self):
        del self.principal

    @property
    def courses(self):
        return self.__courses

    @property
    def min_students(self):
        return self.__min_students

    @min_students.setter
    def min_students(self, value):
        if self.__max_students == 0:
            print("\nDebe establecer primero la cantidad máxima de estudiantes que tendra el programa.")
        elif value > self.__max_students:
            print(f"\nLa cantidad mínima de estudiantes del programa debe ser menor a la cantidad máxima de estudiantes, la cual es: \"{self.__max_students}\"")
        elif value < 0:
            print("\nLa cantidad mínima de estudiantes del programa debe ser mayor o igual a 0.")
        else:
            self.__min_students = value
            
    @min_students.deleter
    def min_students(self):
        del self.__min_students

    @property
    def max_students(self):
        return self.__max_students

    @max_students.setter
    def max_students(self, value):
        if value <= 0:
            print("\nLa cantidad máxima de estudiantes del programa no puede ser 0 o menor que 0.")
        elif value < self.__min_students:
            print(f"\nLa cantidad máxima de estudiantes del programa debe ser mayor a la cantidad mínima de estudiantes, la cual es: \"{self.__min_students}\"")
        else:
            self.__max_students = value

    @max_students.deleter
    def max_students(self):
        del self.__max_students

    @property
    def min_courses(self):
        return self.__min_courses

    @min_courses.setter
    def min_courses(self, value):
        if self.__max_courses == 0:
            print("\nDebe establecer primero la cantidad máxima de cursos que tendra el programa.")
        elif value > self.__max_courses:
            print(f"\nLa cantidad mínima de cursos del programa debe ser menor a la cantidad máxima de cursos, la cual es: \"{self.__max_courses}\"")
        elif value < 0:
            print("\nLa cantidad mínima de cursos del programa debe ser mayor o igual a 0.")        
        else:
            self.__min_courses = value

    @min_courses.deleter
    def min_courses(self):
        del self.__min_courses

    @property
    def max_courses(self):
        return self.__max_courses

    @max_courses.setter
    def max_courses(self, value):
        if value <= 0:
            print("\nLa cantidad máxima de cursos del programa no puede ser 0 o menor que 0.")
        elif value < self.__min_courses:
            print(f"\nLa cantidad máxima de cursos del programa debe ser mayor a la cantidad mínima de cursos, la cual es: \"{self.__min_courses}\"")
        else:
            self.__max_courses = value

    @max_courses.deleter
    def max_courses(self):
        del self.__max_courses

    @property
    def program_duration(self):
        return self.__program_duration

    @program_duration.setter
    def program_duration(self, value):
        if value == 5 or value == 4:
            self.__program_duration = value
        else:
            print("\nLa duración del programa únicamente puede ser 5 o 4 años.")

    @program_duration.deleter
    def program_duration(self):
        del self.__program_duration
    
    def add_course(self, course):
        if (len(self.__courses) + 1) > self.__max_courses:
            return print("No es posible agregar mas cursos al programa {}. El programa ya ha alcanza su cuota máxima de cursos".format( self.__program_name))
        else:
            for i in range(0, len(self.__courses),1):
                if course.course_name == self.__courses[i].course_name:
                    return print("Ya existe un curso con el nombre {} en el programa {}".format(course.course_name, self.__program_name))
            
            self.__courses.append(course)
            return print("Curso {} agregado existosamente al programa {}".format(course.course_name, self.__program_name))
