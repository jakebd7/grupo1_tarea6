import random

class Person:
    
    instances_teacher = []
    instances_student = []

    def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, age = None, email = None):
        self.__name = name
        self.__last_name = last_name
        self.__identification = identification
        self.__address = address
        self.__phone_number = phone_number
        self.__date_birth = date_birth
        self.__age = age
        self.__email = email
        self.__max_courses = 0
        self.__min_courses = 0
        self.__courses = []

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if len(self.__courses) <= self.__max_courses:
            self.__courses.append(value)

    @courses.deleter
    def courses(self):
        del self.__courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @last_name.deleter
    def last_name(self):
        del self.__last_name

    @property
    def identification(self):
        return self.__identification

    @identification.setter
    def identification(self, value):
        if value < 0:
            print("\nEl número de cédula debe ser un número entero positivo.") 
        else: 
            self.__identification = value

    @identification.deleter
    def identification(self):
        del self.__identification

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        self.__address = value

    @address.deleter
    def address(self):
        del self.__address

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value < 0:
            print("\nEl número telefónico debe ser un número entero positivo.") 
        else:                   
            self.__phone_number = value

    @phone_number.deleter
    def phone_number(self):
        del self.__phone_number

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 16:
            self.__age = value
        else:
            return print("\nLos estudiantes y profesores deben tener una edad igual o superior a 16 años.")

    @age.deleter
    def age(self):
        del self.__age

    @property
    def date_birth(self):
        return self.__date_birth

    @date_birth.setter
    def date_birth(self, value):
        self.__date_birth = value

    @date_birth.deleter
    def date_birth(self):
        del self.__date_birth

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email

    @property
    def min_courses(self):
        return self.__min_courses

    @min_courses.setter
    def min_courses(self, value):
        if self.__max_courses == 0:
            print("\nDebe establecer primero la cantidad máxima de cursos.")
        elif value > self.__max_courses:
            print(f"\nLa cantidad mínima de cursos debe ser menor a la cantidad máxima de cursos, la cual es: \"{self.__max_courses}\"")
        elif value < 0:
            print("\nLa cantidad mínima de cursos debe ser mayor o igual a 0.")        
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
            print("\nLa cantidad máxima de cursos no puede ser 0 o menor que 0.")
        elif value < self.__min_courses:
            print(f"\nLa cantidad máxima de cursos debe ser mayor a la cantidad mínima de cursos, la cual es: \"{self.__min_courses}\"")
        else:
            self.__max_courses = value

    @max_courses.deleter
    def max_courses(self):
        del self.__max_courses

    def __str__(self):
        return "Persona"

    def create_person(type):
        class Teacher(Person):

            def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, email = None):
                super(Teacher, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_teacher = int("{}{}{}".format(random.randint(10,99), random.randint(10,99), random.randint(10,99)))
                self.__teacher_type = "No Establecido"
                self.__turn = "No Establecido"
                Person.instances_teacher.append(self)

            @property
            def teacher_type(self):
                return self.__teacher_type

            @teacher_type.setter
            def teacher_type(self, value):
                self.__teacher_type = value

            @teacher_type.deleter
            def teacher_type(self):
                del self.__teacher_type

            @property
            def turn(self):
                return self.__turn

            @turn.setter
            def turn(self, value):
                self.__turn = value

            @turn.deleter
            def turn(self):
                del self.__turn

            @property
            def id_teacher(self):
                return self.__id_teacher

            @id_teacher.setter
            def id_teacher(self, value):
                self.__id_teacher = value

            @id_teacher.deleter
            def id_teacher(self):
                del self.__id_teacher

        class Student(Person):
            def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, email = None):
                super(Student, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_student = int("{}{}{}".format(random.randint(10,99), random.randint(10,99), random.randint(10,99)))
                self.__discount_grades = 1
                Person.instances_student.append(self)
   
            @property
            def id_student(self):
                return self.__id_student

            @id_student.setter
            def id_student(self, value):
                self.__id_student = value

            @id_student.deleter
            def id_student(self):
                del self.__id_student            
            
            def enroll(self, tuition):
                for course in tuition.courses_students:
                    if self.__id_student in tuition.courses_students[course]:
                        print("Estudiante con id {} esta matriculado.".format(self.__id_student))
                        return True

                return False

            def total_cost(self, tuition):
                
                program_name = str
                no_discount = False
                discount_duration = 1
                total_pay = 0

                for program_name in tuition.programs_students:
                    if self.__id_student in tuition.programs_students[program_name]:
                        for i in tuition.programs:
                            if i.program_name == program_name:
                                if i.program_duration == 5:
                                    discount_duration = 0.9
                                elif i.program_duration == 4:
                                    discount_duration = 0.95
                                else:
                                    return print("El programa de estudios no tiene duración de 5 o 4 años.")
                                break
                        break
                        
                for course in tuition.courses_students:
                    if self.__id_student in tuition.courses_students[course]:
                        for i in tuition.courses:
                            if i.course_name == course:
                                total_pay += (i.price * discount_duration) 

                total_pay *= self.__discount_grades

                for course in tuition.courses_students:
                    if self.__id_student in tuition.courses_students[course]:
                        if  tuition.courses_students[course][self.__id_student] == None:
                            pass
                        elif tuition.courses_students[course][self.__id_student] < 90:
                            no_discount = True

                if no_discount == False:
                    self.__discount_grades = 0.9 # descuento del 10 %
                else:
                    self.__discount_grades = 1    

                return total_pay

        if (type == "Teacher"):
            return Teacher()
        if (type == "Student"):
            return Student()

