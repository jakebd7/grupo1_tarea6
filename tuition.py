import time

from program import Program

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
    
    @courses_students.setter
    def courses_students(self, value):
        self.__courses_students = value

    @property
    def programs_students(self):
        return self.__programs_students

    @programs_students.setter
    def programs_students(self, value):
        self.__programs_students = value

    @property
    def credits_students(self):
        return self.__credits_students

    def add_program(self, program, student):
        self.__programs = getattr(program, "instances")
        self.__students = getattr(student,"instances_student")

        if not (program.program_name in self.__programs_students):
            for program_name in self.__programs_students:
                if student.id_student in self.__programs_students[program_name]:
                    print(f"\nEl estudiante con id \"{student.id_student}\" se encuentra inscrito en el programa \"{program_name}\". El estudiante no sera inscrito en otro programa.")
                    return False
                
            self.__programs_students[program.program_name] = [student.id_student]
            
        else:
            if student.id_student in self.__programs_students[program.program_name]:
                print(f"\nEl estudiante con id \"{student.id_student}\" ya se encuentra inscrito en este programa.")
                return False
            elif (len(self.__programs_students[program.program_name]) < program.max_students):
                self.__programs_students[program.program_name].append(student.id_student)
            else:
                print(f"\nNo es posible agregar mas estudiantes al programa \"{program.program_name}\". Cuota máxima de estudiantes alcanzada.")
                return False                

        if (len(self.__programs_students[program.program_name]) < program.min_students):
            program.program_status = "No Aperturado"
        else:
            program.program_status = "Aperturado"            
        
        print(f"\nEstudiante inscrito exitosamente en el programa \"{program.program_name}\".")
        return True

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
            print("\nEl estudiante debe estar inscrito en algun programa para ser agregado en algun curso.")
            return False
        
        for program in Program.instances:
            if program_name == program.program_name:
                if not (course in program.courses):
                    print(f"\nEl curso \"{course.course_name}\" no se encuentra agregado en el programa \"{program.program_name}\", programa en el que se encuentra inscrito el estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\".")
                    return False

        # Verificar que el programa tiene la cantidad minima de cursos establecidos
        for program in self.__programs:
            if program.program_name == program_name:
                if (len(program.courses) < program.min_courses):
                    print(f"\nEl programa \"{program.program_name}\" aun no cuenta con la cantidad mínima de cursos requerida para que se inscriban estudiantes.")
                    return False

        # Verificar que el estudiante no ha excedido la capacida máxima de cursos que puede tomar
        course_student_counter = len([x for x in self.__courses_students if student.id_student in self.__courses_students[x]])

        if course_student_counter > student.max_courses:
            print(f"\nNo es posible inscribir mas cursos al estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\". Cuota máxima de cursos alcanzada previamente.")
            return False                                             

        # Verificar que el curso esta dentro del programa al que esta inscrito el estudiante
        for program in self.__programs:
            if program.program_name == program_name:
                if not (course in program.courses):
                    print(f"\nNo existe un curso con el nombre \"{course.course_name}\" en el programa que se encuentra inscrito el estudiante.")
                    return False
        
        # Agregar estudiante a un curso
        if not (course.course_name in self.__courses_students):
            self.__courses_students[course.course_name] = {student.id_student: None}
            course.course_status = "No Aperturado"
            print(f"\nEl estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\" fue agregado exitosamente al curso \"{course.course_name}\".")
            return True

        elif student.id_student in self.__courses_students[course.course_name]:
            print(f"\nEl estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\" ya se encuentra inscrito en el curso \"{course.course_name}\".")
            return False

        elif (len(self.__courses_students[course.course_name]) <= course.max_students):
            self.__courses_students[course.course_name][student.id_student] = None
            if (len(self.__courses_students[course.course_name]) >= course.min_students):
                course.course_status = "Aperturado" 
            print(f"\nEl estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\" fue agregado exitosamente al curso \"{course.course_name}\".")

            course_student_counter = len([x for x in self.__courses_students if student.id_student in self.__courses_students[x]])
            
            if course_student_counter < student.min_courses:
                print(f"\nEl estudiante \"{student.name} {student.last_name}\" con id \"{student.id_student}\" aun no ha inscrito la cantidad mínima de \"{student.min_courses}\" cursos requerido.")   

            return True

        else:
            print(f"\nNo es posible agregar mas estudiantes al curso \"{course.course_name}\". Cuota máxima de estudiantes alcanzada previamente.")
            return True

    def add_note(self, course, student, note):
       
        if not (course.course_name in self.__courses_students):
            print(f"\nNo existe el curso \"{course.course_name}\".")
            return False
        elif not(student.id_student in self.__courses_students[course.course_name]):
            print(f"No existe un estudiante con el id \"{student.id_student}\".")
            return False
        elif course.credits == None:
            print(f"\nNo ha establecido los creditos del curso \"{course.course_name}\".")
            return False
        else:
            self.__courses_students[course.course_name][student.id_student] = note
            if self.__courses_students[course.course_name][student.id_student] >= 60:
                if not (student.id_student in self.__credits_students):
                    self.__credits_students[student.id_student] = course.credits
                else:
                    self.__credits_students[student.id_student] += course.credits
            print("\nNota agregada exitosamente.")
            return True

    def total_fee(self, mode = 0):
        total_pay = 0
        
        if len(self.__courses_students) == 0:
            if mode == 0:
                print("\nNo hay estudiantes inscritos en cursos.")
            return total_pay
        
        for course in self.__courses:
            try:
                total_pay += (len(self.__courses_students[course.course_name]) * course.price)
            except KeyError:
                continue

        return total_pay

    def __str__(self):
        return "Matricula"