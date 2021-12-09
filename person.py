import tuition

class Person:
    
    def __init__(self, name = "None", last_name = "None", identification = "None", address = "None", phone_number = "None", date_birth = "None", email = "None", min_courses = "None", max_courses = "None"):
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
            def __init__(self, name = "None", last_name = "None", identification = "None", address = "None", phone_number = "None", date_birth = "None", email = "None", id_teacher = "None"):
                super(Teacher, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_teacher = id_teacher
                self.__courses = []

            @property
            def id_teacher(self):
                return self.__id_teacher

            @id_teacher.setter
            def id_teacher(self, value):
                self.__id_teacher = value

            @id_teacher.deleter
            def id_teacher(self):
                del self.__id_teacher

            @property
            def courses(self):
                return self.__courses

            @courses.setter
            def courses(self, value):
                self.__courses.append(value)

            @courses.deleter
            def courses(self):
                del self.__courses

            def create_teacher(self):
                print("Create teacher placeholder")

        class Student(Person):
            def __init__(self, name = "None", last_name = "None", identification = "None", address = "None", phone_number = "None", date_birth = "None", email = "None", id_student = "None"):
                super(Student, self).__init__(name, last_name, identification, address, phone_number, date_birth , email)
                self.__id_student = id_student
                self.__courses = {}
   
            @property
            def id_student(self):
                return self.__id_student

            @id_student.setter
            def id_student(self, value):
                self.__id_student = value

            @id_student.deleter
            def id_student(self):
                del self.__id_student
            
            @property
            def courses(self):
                return self.__courses
    
            @courses.setter
            def courses(self, value):
                self.__courses[value] = value

            @courses.deleter
            def courses(self):
                del self.__courses            
            
            def enroll(self):
                if len(self.__courses) <= 6:
                    return True
                else:
                    return False

            def total_cost(self):

                print("Placeholder for total_fee.")

        if (type == "Teacher"):
            return Teacher()
        if (type == "Student"):
            return Student()

