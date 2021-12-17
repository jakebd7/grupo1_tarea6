class Course:
    instances = []

    def __init__(self, course_name = None, credits = None, week_hours = None, program = None, price = None, teacher = None, course_status = None):
        self.__course_name = course_name
        self.__credits = credits
        self.__week_hours = week_hours
        self.__program = program
        self.__price = price
        self.__teacher = teacher
        self.__course_status = course_status
        self.__min_students = 0
        self.__max_students = 0
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
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        teacher_counter = 0
        for course in self.__class__.instances:
            if None == course.teacher:
                pass
            elif teacher.id_teacher == course.teacher.id_teacher:
                teacher_counter += 1
        
        if teacher_counter < teacher.min_courses -1:            
            self.__teacher = teacher
            print("El profesor de nombre {} con id {}, aun no ha alcanzado su cuota minima de cursos.".format(teacher.name, teacher.id_teacher))    
        elif teacher_counter >= teacher.max_courses:
            return print("No se pueden agregar mas cursos al profesor de nombre {} con id {}, su cuota máxima de cursos ha sido alcanzada previamente.".format(teacher.name, teacher.id_teacher))
        else:
            self.__teacher = teacher

    @teacher.deleter
    def teacher(self):
        del self.__teacher

    @property
    def course_status(self):
        return self.__course_status

    @course_status.setter
    def course_status(self, value):
        self.__course_status = value

    @course_status.deleter
    def course_status(self):
        del self.__course_status

    @property
    def min_students(self):
        return self.__min_students

    @min_students.setter
    def min_students(self, value):
        if self.__max_students == 0:
            return print("Debe establecer primero la cantidad máxima de estudiantes que tendra el programa.")
        elif value > self.__max_students:
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
