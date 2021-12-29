import time

class Tuition:
    instances = []

    def __init__(self,name = None):
        self.__name = name
        self.__tuition_date = time.strftime("%d/%m/%y")
        self.__tuition_hour = time.strftime("%H%M%S")
        self.__students = []
        self.__courses = []
        self.__programs = []
        self.__courses_students = {}
        self.__programs_students = {}
        self.__credits_students = {}
        self.__class__.instances.append(self)
  
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
    def tuition_date(self):
        return self.__tuition_date

    @tuition_date.setter
    def tuition_date(self, value):
        self.__tuition_date = value

    @tuition_date.deleter
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

    @property
    def courses(self):
        return self.__courses

    @property
    def programs(self):
        return self.__programs
    
    @property
    def courses_students(self):
        return self.__courses_students
    
    @property
    def programs_students(self):
        return self.__programs_students

    @property
    def credits_students(self):
        return self.__credits_students

    def add_program(self, program, student):
        self.__programs = getattr(program, "instances")
        self.__students = getattr(student,"instances_student")

        if not (program.program_name in self.__programs_students):
            for program_name in self.__programs_students:
                if student.id_student in self.__programs_students[program_name]:
                    return print("El estudiante con id {} se encuentra inscrito en el programa {}. El estudiante no sera inscrito en otro programa".format(student.id_student, program_name))
                
            self.__programs_students[program.program_name] = [student.id_student]
            
        else:
            if student.id_student in self.__programs_students[program.program_name]:
                return print("El estudiante con id {} ya se encuentra inscrito en este programa.".format(student.id_student))
            elif (len(self.__programs_students[program.program_name]) < program.max_students):
                self.__programs_students[program.program_name].append(student.id_student)
            else:
                return print("No es posible agregar mas estudiantes al programa {}. Cuota máxima de estudiantes alcanzada.".format(program.program_name))                

        if (len(self.__programs_students[program.program_name]) < program.min_students):
            program.program_status = "No Aperturado"
        else:
            program.program_status = "Aperturado"            
        
        return print("Estudiante inscrito exitosamente en el programa {}.".format(program.program_name))

    def add_course(self, course, student):
        self.__courses = getattr(course,"instances")

        program_name = None
        course_student_counter = 0

        # Verificar que el estudiante este inscrito a un programa
        for program in self.__programs_students:
            if student.id_student in self.__programs_students[program]:
                program_name = program
                break

        if program_name == None:
            print("El estudiante debe estar inscrito en algun programa para ser agregado en algun curso.")
        
        # Verificar que el programa tiene la cantidad minima de cursos establecidos
        for program in self.__programs:
            if program.program_name == program_name:
                if (len(program.courses) < program.min_courses):
                    print("El programa aun no cuenta con la cantidad minima de cursos para que se inscriban estudiantes.")

        # Verificar que el estudiante no ha excedido la capacida máxima de cursos que puede tomar
        for course_x in self.__courses_students:
            if student.id_student in self.__courses_students[course_x]:
                course_student_counter += 1

        if course_student_counter >= student.max_courses:
            print("No es posible inscribir mas cursos al estudiante de nombre {} con id {}. Cuota máxima de cursos alcanzada.".format(student.name, student.id_student))
        elif course_student_counter == 0:
            pass
        elif course_student_counter < student.min_courses:
            print("El estudiante de nombre {} con id {} aun no ha inscrito la cantidad minima de {} cursos requerido.".format(student.name, student.id_student, student.min_courses))
            
        # Verificar que el curso esta dentro del programa al que esta inscrito el estudiante
        for program in self.__programs:
            if program.program_name == program_name:
                if not (course in program.courses):
                    print("No existe un curso con el nombre {} en el programa que se encuentra inscrito el estudiante.".format(course.course_name))
        
        # Agregar estudiante a un curso
        if not (course.course_name in self.__courses_students):
            self.__courses_students[course.course_name] = {student.id_student: None}
            course.course_status = "No Aperturado"
            print("El estudiante de nombre {} con id {} fue agregado exitosamente al curso {}".format(student.name, student.id_student, course.course_name))
        elif student.id_student in self.__courses_students[course.course_name]:
            print("El estudiante de nombre {} con id {} ya se encuentra inscrito en el curso {}.".format(student.name, student.id_student, course.course_name))
        elif (len(self.__courses_students[course.course_name]) <= course.max_students):
            self.__courses_students[course.course_name][student.id_student] = None
            if (len(self.__courses_students[course.course_name]) >= course.min_students):
                course.course_status = "Aperturado" 
            print("El estudiante de nombre {} con id {} fue agregado exitosamente al curso {}".format(student.name, student.id_student, course.course_name))

        else:
            print("No es posible agregar mas estudiantes al curso {}. Cuota máxima de estudiantes alcanzada.".format(course.course_name))

    def add_note(self, course, student, note):
       
        if not (course.course_name in self.__courses_students):
            print("No existe el curso {}.".format(course.course_name))
        elif not(student.id_student in self.__courses_students[course.course_name]):
            print("No existe un estudiante con el id {}.".format(student.id_student))
        elif course.credits == None:
            print("No ha establecido los creditos del curso {}.".format(course.course_name))
        else:
            self.__courses_students[course.course_name][student.id_student] = note
            if self.__courses_students[course.course_name][student.id_student] >= 60:
                if not (student.id_student in self.__credits_students):
                    self.__credits_students[student.id_student] = course.credits
                else:
                    self.__credits_students[student.id_student] += course.credits
            print("Nota agregada exitosamente.")

    def total_fee(self):
        total_pay = 0
        
        if len(self.__courses_students) == 0:
            print("No hay estudiantes inscritos a cursos.")
            return total_pay
        
        for course in self.__courses:
            total_pay += (len(self.__courses_students[course.course_name]) * course.price)

        return total_pay

    def __str__(self):
        return "Matricula"