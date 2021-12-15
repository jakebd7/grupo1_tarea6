import random

class Person:
    
    instances_teacher = []
    instances_student = []

    def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, email = None, min_courses = None, max_courses = None):
        self.__name = name
        self.__last_name = last_name
        self.__identification = identification
        self.__address = address
        self.__phone_number = phone_number
        self.__date_birth = date_birth
        self.__email = email
        self.__min_courses = min_courses
        self.__max_courses = max_courses

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
        self.__phone_number = value

    @phone_number.deleter
    def phone_number(self):
        del self.__phone_number

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
        self.__min_courses = value

    @min_courses.deleter
    def min_courses(self):
        del self.__min_courses

    @property
    def max_courses(self):
        return self.__max_courses

    @max_courses.setter
    def max_courses(self, value):
        self.__max_courses = value

    @max_courses.deleter
    def max_courses(self):
        del self.__max_courses

    def create_person(type):
        class Teacher(Person):

            def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, email = None, id_teacher = None):
                super(Teacher, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_teacher = int("{}{}{}".format(random.randint(10,99), random.randint(10,99), random.randint(10,99)))
                Person.instances_teacher.append(self)
            @property
            def id_teacher(self):
                return self.__id_teacher

            @id_teacher.setter
            def id_teacher(self, value):
                self.__id_teacher = value

            @id_teacher.deleter
            def id_teacher(self):
                del self.__id_teacher

            def create_teacher(self):
                print("Create teacher placeholder")

        class Student(Person):
            def __init__(self, name = None, last_name = None, identification = None, address = None, phone_number = None, date_birth = None, email = None):
                super(Student, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_student = int("{}{}{}".format(random.randint(10,99), random.randint(10,99), random.randint(10,99)))
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
                discount = int
                total_pay = 0

                for program_name in tuition.programs_students:
                    if self.__id_student in tuition.programs_students[program_name]:
                        for i in tuition.programs:
                            if i.program_name == program_name:
                                if i.program_duration == 5:
                                    discount = 0.9
                                elif i.program_duration == 4:
                                    discount = 0.95
                                else:
                                    return print("El programa de estudios no tiene duración de 5 o 4 años.")
                                break
                        break
                        
                for course in tuition.courses_students:
                    if self.__id_student in tuition.courses_students[course]:
                        for i in tuition.courses:
                            if i.course_name == course:
                                total_pay += (i.price * discount) 

                return total_pay

        if (type == "Teacher"):
            return Teacher()
        if (type == "Student"):
            return Student()

