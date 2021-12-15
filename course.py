class Course:
    instances = []

    def __init__(self, course_name = None, credits = None, week_hours = None, program = None, price = None,min_students = None, max_students = None):
        self.__course_name = course_name
        self.__credits = credits
        self.__week_hours = week_hours
        self.__program = program
        self.__price = price
        self.__min_students = min_students
        self.__max_students = max_students
        self.__class__.instances.append(self)

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        self.__course_name = value

    @course_name.deleter
    def course_name(self):
        del self.__course_name

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        self.__credits = value

    @credits.deleter
    def credits(self):
        del self.__credits

    @property
    def week_hours(self):
        return self.__week_hours

    @week_hours.setter
    def week_hours(self, value):
        self.__week_hours = value

    @week_hours.deleter
    def week_hours(self):
        del self.__week_hours

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        self.__program = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price

    @property
    def min_students(self):
        return self.__min_students

    @min_students.setter
    def min_students(self, value):
        if self.__min_students == 0:
            return print("Debe establecer primero la cantidad máxima de estudiantes que tendra el programa.")
        elif value > self.__min_students:
            return print("La cantidad minima de estudiantes del programa debe ser menor a la cantidad máxima de estudiantes.")
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
        if value < self.__min_students:
            return print("La cantidad máxima de estudiantes del programa debe ser mayor a la cantidad minima de estudiantes.")
        else:
            self.__max_students = value

    @max_students.deleter
    def max_students(self):
        del self.__max_students


#class A:
#    instances = []
#    def __init__(self):
#        self.__class__.instances.append(self)
#print('\n'.join(A.instances))