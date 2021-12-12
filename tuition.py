import time

class Tuition:
    def __init__(self,):
        self.__tuition_date = time.strftime("%d/%m/%y")
        self.__tuition_hour = time.strftime("%H%M%S")
        self.__students = []
        self.__courses = []
        self.__courses_students = {}
  
    @property
    def tuition_date(self):
        return self.__tuition_date

    @tuition_date.setter
    def tuition_date(self, value):
        self.__tuition_date = value

    @tuition_date.setter
    def tuition_date(self):
        del self.__tuition_date

    @property
    def tuition_hour(self):
        return self.__tuition_hour

    @tuition_hour.setter
    def tuition_hour(self, value):
        self.__tuition_hour = value

    @tuition_hour.deleter
    def tuition_hour(self):
        del self.__tuition_hour

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        self.__students.append(value)

    @students.setter
    def students(self):
        del self.__students

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.__courses.append(value)

    @courses.setter
    def courses(self):
        del self.__courses

    @property
    def courses_students(self):
        return self.__courses_students
    
    def add_course(self, course, student):
        self.__courses.append(getattr(course,'instances'))
        self.__students.append(getattr(student,'instances'))
        if (course.course_name in self.__courses_students) == False:
            self.__courses_students[course.course_name] = {student.id_student: None}
        else:
            self.__courses_students[course.course_name][student.id_student] = None

    def add_note(self, course, student, note):
        self.__courses_students[course][student.id_student] = note

    def total_fee(self):
        for i in self.__courses:
            print("El nombre del curso es: {}".format(i.course_name))
        #total = 0
        #for course in self.__courses:
        #    total = total + (len(self.__courses_students[course.course_name]) * course.price)

        #return total