import time

class Tuition:
    def __init__(self,):
        self.__tuition_date = time.strftime("%d/%m/%y")
        self.__tuition_hour = time.strftime("%H%M%S")
        self.__students = []
        self.__courses = []
        self.__programs = []
        self.__courses_students = {}
        self.__programs_students = {}
  
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

    def add_program(self, program, student):
        self.__programs = getattr(program, "instances")
        self.__students = getattr(student,"instances_student")

        for program_obj in self.__programs:
            if program.program_name == program_obj.program_name:
                if len(self.__programs_students[program.program_name]) < program_obj.min_students:
                    program_obj.program_status = "No Aperturado"
                elif len(self.__programs_students[program.program_name]) > program_obj.max_students:
                    program_obj.program_status = "Aperturado"
                    return print("No es posible agregar mas estudiantes al programa {}. Cuota máxima de estudiantes alcanzada.".format(program.program_name))
                else:
                    program_obj.program_status = "Aperturado"

        if not (program.program_name in self.__programs_students):
            for program_name in self.__programs_students:
                if student.id_student in self.__programs_students[program_name]:
                    return print("El estudiante con id {} se encuentra inscrito en el {}. El estudiante no sera inscrito en otro programa".format(student.id_student, program_name))
                
            self.__programs_students[program.program_name] = [student.id_student]
            
        else:
            if student.id_student in self.__programs_students[program.program_name]:
                return print("El estudiante con id {} ya se encuentra inscrito en este programa.".format(student.id_student))
            else:
                self.__programs_students[program.program_name].append(student.id_student)
        
        return print("Estudiante inscrito exitosamente en el programa {}.".format(program.program_name))

    def add_course(self, course, student):
        self.__courses = getattr(course,"instances")

        program_name = None

        # Seteo del atributo course_status del objeto course
        for course_obj in self.__courses:
            if course.course_name == course_obj.course_name:
                if len(self.__courses_students[course.course_name]) < course_obj.min_students:
                    course_obj.course_status = "No Aperturado"
                elif len(self.__courses_students[course.course_name]) > course_obj.max_students:
                    course_obj.course_status = "Aperturado"
                    return print("No es posible agregar mas estudiantes al programa {}. Cuota máxima de estudiantes alcanzada.".format(course.course_name))
                else:
                    course_obj.course_status = "Aperturado"

        # Verificar que el estudiante este inscrito a un programa
        for program in self.__programs_students:
            if student.id_student in self.__programs_students[program]:
                program_name = program
                break

        if program_name == None:
            return print("El estudiante debe estar inscrito en algun programa para ser agregado en algun curso.")
        
        # Verificar que el programa tiene la cantidad minima de cursos establecidos
        for program in self.__programs:
            if program.program_name == program_name:
                if (len(program.courses) <= program.min_courses):
                    return print("El programa aun no cuenta con la cantidad minima de cursos para que se inscriban estudiantes.")
        
        # Verificar que el curso esta dentro del programa al que esta inscrito el estudiante
        for program in self.__programs:
            if program.program_name == program_name:
                if not (course.course_name in program.courses):
                    return print("No existe un curso con el nombre {} en el programa que se encuentra inscrito el estudiante.".format(course.course_name))
        
        # Agregar estudiante a un curso
        if not (course.course_name in self.__courses_students):
            self.__courses_students[course.course_name] = {student.id_student: None}
            return print("Estudiante con id {} agregado exitosamente al curso {}".format(student.id_student, course.course_name))
        elif student.id_student in self.__courses_students[course.course_name]:
            return print("El estudiante con id {} ya se encuentra inscrito en el curso {}.".format(student.id_student, course.course_name))
        else:
            self.__courses_students[course.course_name][student.id_student] = None
            return print("Estudiante con id {} agregado exitosamente al curso {}".format(student.id_student, course.course_name))

    def add_note(self, course, student, note):
       
        if not (course.course_name in self.__courses_students):
            return print("No existe el curso {}.".format(course.course_name))
        elif not(student.id_student in self.__courses_students[course.course_name]):
            return print("No existe un estudiante con el id {}.".format(student.id_student))
        else:
            self.__courses_students[course.course_name][student.id_student] = note
            return print("Nota agregada exitosamente.")


    def total_fee(self):
        total_pay = 0
        
        if len(self.__courses_students) == 0:
            print("No hay estudiantes inscritos a cursos.")
            return total_pay
        
        for course in self.__courses:
            total_pay += (len(self.__courses_students[course.course_name]) * course.price)

        return total_pay