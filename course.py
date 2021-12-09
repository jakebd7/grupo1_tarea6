class Course:
    def __init__(self, course_name = "None", credits = "None", week_hours = "None", program = "None", min_students = "None", max_students = "None"):
        self.__course_name = course_name
        self.__credits = credits
        self.__week_hours = week_hours
        self.__program = program
        self.__min_students = min_students
        self.__max_students = max_students

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
    def min_students(self):
        return self.__min_students

    @min_students.setter
    def min_students(self, value):
        self.__min_students = value

    @min_students.deleter
    def min_students(self):
        del self.__min_students

    @property
    def max_students(self):
        return self.__max_students

    @max_students.setter
    def max_students(self, value):
        self.__max_students = value

    @max_students.deleter
    def max_students(self):
        del self.__max_students
    
    @program.deleter
    def program(self):
        del self.__program