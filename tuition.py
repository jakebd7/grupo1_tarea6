import time

class Tuition:
    def __init__(self, student = "None"):
        self.__student = student
        self.__tuition_date = time.strftime("%d/%m/%y")
        self.__tuition_hour = time.strftime("%H%M%S")
        self.__students_counter = 0
  
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

    def add_course(self, course):
        self.__student.courses[course.course_name] = "None"

    def add_note(self, course, note):
        self.__student.courses[course.course_name] = note

    def total_fee(self, fees):
        pass