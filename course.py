class Course:
    instances = []

    def __init__(self, course_name = None, credits = None, week_hours = None, price = None):
        self.__course_name = course_name
        self.__credits = credits
        self.__week_hours = week_hours
        self.__program = "No Establecido"
        self.__price = price
        self.__teacher = "No Establecido"
        self.__course_status = "No Aperturado"
        self.__max_students = 0
        self.__min_students = 0
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
        if value < 0:
            print("\nLa cantidad de creditos del curso debe ser un número entero positivo mayor o igual a 0.")
        else:            
            self.__credits = value

    @credits.deleter
    def credits(self):
        del self.__credits

    @property
    def week_hours(self):
        return self.__week_hours

    @week_hours.setter
    def week_hours(self, value):
        if value < 0:
            print("\nLa cantidad de horas semanales del curso debe ser un número entero positivo mayor o igual a 0.")
        else:        
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
        if value < 0:
            print("\nEl precio del curso debe ser un número entero positivo mayor o igual a 0.")
        else:
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
            if "No Establecido" == course.teacher:
                pass
            elif teacher.id_teacher == course.teacher.id_teacher:
                teacher_counter += 1
        
        if teacher_counter < teacher.min_courses -1:            
            self.__teacher = teacher            
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name}\" con id \"{teacher.id_teacher}\", fue agregado existosamente al curso {self.__course_name}.")            
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name}\" con id \"{teacher.id_teacher}\", aun no ha alcanzado su cuota mínima de cursos.")    
        
        elif teacher_counter >= teacher.max_courses:
            print(f"\nNo se pueden agregar mas cursos al profesor de nombre \"{teacher.name} {teacher.last_name}\" con id \"{teacher.id_teacher}\", su cuota máxima de cursos ha sido alcanzada previamente.")
        else:
            self.__teacher = teacher
            print(f"\nEl profesor \"{teacher.name} {teacher.last_name}\" con id \"{teacher.id_teacher}\", fue agregado existosamente al curso {self.__course_name}.")

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
            print("\nDebe establecer primero la cantidad máxima de estudiantes que tendra el curso.")
        elif value > self.__max_students:
            print(f"\nLa cantidad mínima de estudiantes del curso debe ser menor a la cantidad máxima de estudiantes, la cual es: \"{self.__max_students}\"")
        elif value < 0:
            print("\nLa cantidad mínima de estudiantes del curso debe ser mayor o igual a 0.")
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
            print("\nLa cantidad máxima de estudiantes del curso no puede ser 0 o menor que 0.")
        elif value < self.__min_students:
            print(f"\nLa cantidad máxima de estudiantes del curso debe ser mayor a la cantidad mínima de estudiantes, la cual es: \"{self.__min_students}\"")
        else:
            self.__max_students = value

    @max_students.deleter
    def max_students(self):
        del self.__max_students

    def __str__(self):
        return "Curso"
