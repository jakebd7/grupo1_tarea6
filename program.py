class Program:
    def __init__(self, program_name = "None", creation_date_program = "None", program_status = "None", principal = "None", min_courses = "None", max_courses = "None"):
        self.__program_name = program_name
        self.__creation_date_program = creation_date_program
        self.__program_status = program_status
        self.__principal = principal
        self.__min_courses = min_courses
        self.__max_courses = max_courses

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

    @courses.setter
    def courses(self, value):
        self.__courses = value

    @courses.deleter
    def courses(self):
        del self.courses    

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
    
    def manage_program(self):
        pass
