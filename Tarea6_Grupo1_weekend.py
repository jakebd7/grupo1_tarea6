__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez, Marco Cordoba'

# ----------------------
# Importación de Módulos
# ----------------------

import copy
from typing import BinaryIO
import frontend_extra
from classroom import Classroom
from person import Person
from tuition import Tuition
from course import Course
from program import Program
from teacher_type import Teacher_type
from turn import Turn
from building import Building
from analitycs import Analitycs
from os import name, system, terminal_size
# from catalogs import *


# --------------------
# Definición de Clases
# --------------------


class TextFormat:
    """ Clase con Código de Escape para los Formato del Texto """
    # https://en.wikipedia.org/wiki/ANSI_escape_code
    RED = "\33[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BOLD_UNDERLINE = BOLD + UNDERLINE
    CLEAR = "\033[0m"


# ---------------------------------------
# Declaración de funciones personalizadas
# ---------------------------------------


def clear_screen():
    """Limpia pantalla dependiendo tipo del sistema operativo"""
    if name == "nt":
        system("cls")
    else:
        system("clear")


def clear_flag():
    """Limpia banderas"""
    global selected_submenu3
    selected_submenu3 = ""
    global selected_submenu2
    selected_submenu2 = ""
    global selected_submenu1
    selected_submenu1 = ""
    global selected_menu
    selected_menu = ""
    clear_screen()


def invalid_selection():
    """Selección invalida"""
    input(f"\n{TextFormat.YELLOW}Selección invalida. Digite cualquier tecla para continuar...{TextFormat.CLEAR}")
    global selected_submenu3
    selected_submenu3 = ""
    global selected_submenu2
    selected_submenu2 = ""
    global selected_submenu1
    selected_submenu1 = ""
    global selected_menu
    selected_menu = ""
    clear_screen()


# Programa 1 de prueba
programa_1 = Program("programa_1")
programa_1.principal = "Jose Lopez"
programa_1.max_students = 25
programa_1.min_students = 10
programa_1.max_courses = 1
programa_1.min_courses = 0
programa_1.program_duration = 4

# Programa 2 de prueba
programa_2 = Program("programa_2")
programa_2.principal = "Maria Perez"
programa_2.max_students = 50
programa_2.min_students = 15
programa_2.max_courses = 75
programa_2.min_courses = 42
programa_2.program_duration = 5

# Programa 3 de prueba
programa_3 = Program("programa_3")
programa_3.principal = "Juan de Arco"
programa_3.max_students = 90
programa_3.min_students = 21
programa_3.max_courses = 78
programa_3.min_courses = 13
programa_3.program_duration = 4

# Profesor 1 de prueba
Juan = Person.create_person("Teacher")
Juan.name = "Juan"
Juan.last_name = "Rodriguez"
Juan.identification = 201123456
Juan.address = "arriba"
Juan.phone_number = 1234
Juan.date_birth = "12/12/21"
Juan.age = 25
Juan.email = "ejemplo@email.com"
Juan.max_courses = 30
Juan.min_courses = 5

# Profesor 2 de prueba
Roberto = Person.create_person("Teacher")
Roberto.name = "Roberto"
Roberto.last_name = "Rios"
Roberto.identification = 456328791
Roberto.address = "abajo"
Roberto.phone_number = 56789
Roberto.date_birth = "23/12/21"
Roberto.age = 58
Roberto.email = "ejemplo2@email.com"
Roberto.max_courses = 1
Roberto.min_courses = 0

# Profesor 3 de prueba
Magdalena = Person.create_person("Teacher")
Magdalena.name = "Magdalena"
Magdalena.last_name = "Llanos"
Magdalena.identification = 254671384
Magdalena.address = "derecha"
Magdalena.phone_number = 45128
Magdalena.date_birth = "01/12/21"
Magdalena.age = 35
Magdalena.email = "ejemplo3@email.com"
Magdalena.max_courses = 2
Magdalena.min_courses = 0

# Estudiante 1 de prueba
Miguel = Person.create_person("Student")
Miguel.name = "Miguel"
Miguel.last_name = "Bose"
Miguel.identification = 421065482
Miguel.address = "al lago"
Miguel.phone_number = 4276
Miguel.date_birth = "25/12/21"
Miguel.age = 23
Miguel.email = "ejemplo8@email.com"
Miguel.max_courses = 14
Miguel.min_courses = 2

# Estudiante 2 de prueba
Carlos = Person.create_person("Student")
Carlos.name = "Carlos"
Carlos.last_name = "Fonseca"
Carlos.identification = 4107127546
Carlos.address = "junto al cine"
Carlos.phone_number = 9713
Carlos.date_birth = "08/12/21"
Carlos.age = 41
Carlos.email = "ejemplo9@email.com"
Carlos.max_courses = 26
Carlos.min_courses = 7

# Estudiante 3 de prueba
Robin = Person.create_person("Student")
Robin.name = "Robin"
Robin.last_name = "Hood"
Robin.identification = 748532156
Robin.address = "cerda del volcan"
Robin.phone_number = 6574
Robin.date_birth = "04/12/21"
Robin.age = 18
Robin.email = "ejemplo10@email.com"
Robin.max_courses = 13
Robin.min_courses = 0

# Curso Matematica de prueba
matematica = Course("matematica")
matematica.credits = 5
matematica.week_hours = 42
#matematica.program = programa_1
matematica.price = 200
#matematica.teacher = Juan
matematica.max_students = 20
matematica.min_students = 10

# Curso robotica de prueba
robotica = Course("robotica")
robotica.credits = 10
robotica.week_hours = 30
#robotica.program = programa_1
robotica.price = 150
#robotica.teacher = "Jose Lopez"
robotica.max_students = 50
robotica.min_students = 5

# Curso ingles de prueba
ingles = Course("ingles")
ingles.credits = 35
ingles.week_hours = 60
#ingles.program = programa_1
ingles.price = 250
#ingles.teacher = "Miguel Bose"
ingles.max_students = 70
ingles.min_students = 26

# Turno Matutio 
matutino = Turn("matutino")

# Turno Vespertino
vespertino = Turn("vespertino")

# Turno Nocturno
nocturno = Turn("nocturno")

# Tipo de Profesor - De planta
planta = Teacher_type("planta")

# Tipo de Profesor - Horaio
horario = Teacher_type("horario")

# Aula 1
aula1 = Classroom("aula1")
aula1.floor_number = 25
aula1.seats_capacity = 30

# Aula 2
aula2 = Classroom("aula2")
aula2.floor_number = 50
aula2.seats_capacity = 40

# Aula 2
aula3 = Classroom("aula3")
aula3.floor_number = 60
aula3.seats_capacity = 50

# ----------------------------------------
# Ejecución de las funciones mediante menú
# ----------------------------------------


system('COLOR')
selected_menu = ""
selected_submenu1 = ""
selected_submenu2 = ""
selected_submenu3 = ""

while selected_menu != "s":
    clear_screen()
    print(f"{TextFormat.GREEN}\n---------------------  PROGRAMACIÓN Y ESPECIALIZACIÓN EN PYTHON  ---------------------\n"
          f"---------------------        Trabajo No. 6  - Grupo No. 1        ---------------------{TextFormat.CLEAR}")
    print(f"{TextFormat.CYAN}\nMENÚ\n{TextFormat.CLEAR}"
          f"[A] {TextFormat.BOLD_UNDERLINE}{TextFormat.BOLD}A{TextFormat.CLEAR}dministrar\n"
          f"[V] {TextFormat.BOLD_UNDERLINE}V{TextFormat.CLEAR}erificar Alumno Activo\n"
          f"[C] {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}alcular Analítica\n"
          f"[S] {TextFormat.BOLD_UNDERLINE}S{TextFormat.CLEAR}alir\n")
    selected_menu = input("Digite una opción del menú: ").lower()
    if selected_menu == "a":
        clear_screen()
        print(f"\n{TextFormat.CYAN}Sub Menú - Administrar Catálogos\n{TextFormat.CLEAR}"
              f"[M] {TextFormat.BOLD_UNDERLINE}M{TextFormat.CLEAR}atriculas\n"
              f"[N] {TextFormat.BOLD_UNDERLINE}N{TextFormat.CLEAR}otas\n"
              f"[E] {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}dificios\n"
              f"[A] {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}ulas\n"
              f"[T] {TextFormat.BOLD_UNDERLINE}T{TextFormat.CLEAR}urnos\n"
              f"[I] T{TextFormat.BOLD_UNDERLINE}i{TextFormat.CLEAR}po de Turnos\n"
              f"[P] {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rogramas\n"
              f"[C] {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}ursos\n"
              f"[O] Pr{TextFormat.BOLD_UNDERLINE}o{TextFormat.CLEAR}fesores\n"
              f"[S] E{TextFormat.BOLD_UNDERLINE}s{TextFormat.CLEAR}tudiantes\n"
              f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
        selected_submenu1 = input("Digite una opción: ").lower()
        if selected_submenu1 in "mneatipcos" and selected_submenu1 != "":
            clear_screen()
            print(f"\n{TextFormat.CYAN}Sub Menú - Acciones\n{TextFormat.CLEAR}"
                  f"[C] {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}rear\n"
                  f"[A] {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}gregar\n"
                  f"[O] C{TextFormat.BOLD_UNDERLINE}o{TextFormat.CLEAR}nsultar\n"
                  f"[M] {TextFormat.BOLD_UNDERLINE}M{TextFormat.CLEAR}odificar\n"
                  f"[E] {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}liminar\n"
                  f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
            selected_submenu2 = input("Digite una opción: ").lower()
            if selected_submenu2 in "caome" and selected_submenu2 != "":
                if selected_submenu2 == "c":
                    if selected_submenu1 == "m":                        
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nueva Matricula{TextFormat.CLEAR}")

                        if len(Tuition.instances) > 0:
                            print(f"\nYa existe una matricula creada, no puede existir mas de una matricula creada a la vez.")
                        else:

                            tuition_name = frontend_extra.name_check_with_numbers("matricula")

                            locals()[tuition_name] = Tuition("matricula")

                            while True:
                                verification = input(f"\nDesea crear la matricula \"{locals()[tuition_name].name}\" (S/N): ").lower()
                                if verification == "s":
                                    print(f"\n{TextFormat.CYAN}La matricula \"{locals()[tuition_name].name}\" se ha creado exitosamente.{TextFormat.CLEAR}")

                                    while True:
                                        informatio_view = input(f"\nDeseea ver la información de la matricula (S/N): ").lower()
                                    
                                        if informatio_view == "s":
                                            frontend_extra.program_information_show(locals()[program_name])
                                            break
                                        elif informatio_view == "n":
                                            break
                                    break
                                elif verification == "n":
                                    print(f"\n{TextFormat.CYAN}El programa \"{locals()[program_name].program_name}\" no se creara.{TextFormat.CLEAR}")
                                    frontend_extra.del_instance_in_class(locals()[program_name])
                                    del locals()[program_name]
                                    break

                    elif selected_submenu1 == "e":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Edificio{TextFormat.CLEAR}")
      
                        building_name = frontend_extra.name_check_with_numbers("edificio")
                        locals()[building_name] = Building(building_name)

                        frontend_extra.name_check_without_instance(locals()[building_name], False, "address")

                        frontend_extra.set_change_attr_number(locals()[building_name], False, "number_of_floors")

                        frontend_extra.set_change_attr_number(locals()[building_name], False, "number_of_classrooms")

                        if len(Classroom.instances) > 0:
                            while True:
                                set_check = input("\nDesea establecer en este momento las aulas que tendra el edificio (S/N): ").lower()
                                if set_check == "s":

                                    frontend_extra.view_each_instance(Classroom.instances[0], "No Establecido", "building_number", 2)

                                    while True:
                                        classroom_name = frontend_extra.name_check_non_existence("aula")
                                        if locals()[classroom_name].building_number == "No Establecido":
                                            if locals()[building_name].add_classroom(locals()[classroom_name]):
                                                locals()[classroom_name].building_number = locals()[classroom_name]
                                            
                                                if (len(locals()[building_name].classrooms) < locals()[building_name].number_of_classrooms) and len([x for x in Classroom.instances if x.building_number == "No Establecido"]) > 0:
                                                    set_check2 = input("\nDesea agregar otra aula (S/N): ").lower()
                                                    if set_check2 == "s":
                                                        continue
                                                    elif set_check2 == "n":
                                                        break
                                                else: 
                                                    break
                                    break
                                elif set_check == "n":

                                    break                               

                        while True:
                            verification = input(f"\nDesea crear el edifcio \"{locals()[building_name].name}\" con la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}El edificio \"{locals()[building_name].name}\" se ha creado exitosamente.{TextFormat.CLEAR}")

                                while True:
                                    informatio_view = input(f"\nDeseea ver la información del edificio (S/N): ").lower()
                                
                                    if informatio_view == "s":
                                        frontend_extra.building_information_show(locals()[building_name])
                                        break
                                    elif informatio_view == "n":
                                        break
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El edificio \"{building_name}\" no se creara.{TextFormat.CLEAR}")
                                                                    
                                if len(locals()[building_name].classrooms) > 0: 
                                    frontend_extra.set_attribute_in_list_in_instance(locals()[building_name], "classrooms", "building_number", "No Establecido") 

                                frontend_extra.del_instance_in_class(locals()[building_name])
                                del locals()[building_name]
                                break

                    elif selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Programa{TextFormat.CLEAR}")
      
                        program_name = frontend_extra.name_check_with_numbers("programa")
                        locals()[program_name] = Program(program_name)

                        frontend_extra.name_check_no_numbers(locals()[program_name], False, "principal")  

                        frontend_extra.max_students_check(locals()[program_name]) 

                        frontend_extra.min_students_check(locals()[program_name]) 

                        frontend_extra.max_courses_check(locals()[program_name])

                        frontend_extra.min_courses_check(locals()[program_name])

                        frontend_extra.program_duration_check(locals()[program_name])                     
                        
                        while True:
                            verification = input(f"\nDesea crear el programa \"{locals()[program_name].program_name}\" con la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}El programa \"{locals()[program_name].program_name}\" se ha creado exitosamente.{TextFormat.CLEAR}")

                                while True:
                                    informatio_view = input(f"\nDeseea ver la información del programa (S/N): ").lower()
                                
                                    if informatio_view == "s":
                                        frontend_extra.program_information_show(locals()[program_name])
                                        break
                                    elif informatio_view == "n":
                                        break
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El programa \"{locals()[program_name].program_name}\" no se creara.{TextFormat.CLEAR}")
                                frontend_extra.del_instance_in_class(locals()[program_name])
                                del locals()[program_name]
                                break
                    
                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Curso{TextFormat.CLEAR}")

                        course_name = frontend_extra.name_check_with_numbers("curso")                              
                        locals()[course_name] = Course(course_name)

                        frontend_extra.set_change_attr_number(locals()[course_name], False, "credits")

                        frontend_extra.set_change_attr_number(locals()[course_name], False, "week_hours")

                        if len(Program.instances) > 0:
                            while True:
                                set_check = input("\nDesea establecer en este momento el programa al que pertenecera el curso (S/N): ").lower()
                                if set_check == "s":

                                    frontend_extra.view_each_instance(Program.instances[0], "courses", "max_courses", 1)

                                    while True:
                                        program_name = frontend_extra.name_check_non_existence("programa")
                                        if len (locals()[program_name].courses) < locals()[program_name].max_courses:
                                            if locals()[program_name].add_course(locals()[course_name]):
                                                locals()[course_name].program = locals()[program_name]
                                                break
                                    break
                                elif set_check == "n":

                                    break           

                        frontend_extra.set_change_attr_number(locals()[course_name], False, "price")

                        if len(Person.instances_teacher) > 0:
                            while True:
                                set_check = input("\nDesea establecer en este momento el profesor del curso (S/N): ").lower()
                                if set_check == "s":

                                    frontend_extra.view_each_instance(Person.instances_teacher[0], "courses", "max_courses", 1)  

                                    while True:
                                        teacher_name = frontend_extra.id_check("profesor")
                                        if len (locals()[teacher_name].courses) < locals()[teacher_name].max_courses:
                                            locals()[course_name].teacher = locals()[teacher_name]
                                            if locals()[course_name].teacher != "No Establecido":
                                                locals()[teacher_name].courses = locals()[course_name]
                                                break

                                    break
                                elif set_check == "n":

                                    break

                        frontend_extra.max_students_check(locals()[course_name])

                        frontend_extra.min_students_check(locals()[course_name])

                        while True:
                            verification = input(f"\nDesea crear el curso \"{locals()[course_name].course_name}\" con la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}El curso \"{locals()[course_name].course_name}\" se ha creado exitosamente.{TextFormat.CLEAR}")

                                while True:
                                    informatio_view = input(f"\nDeseea ver la información del curso (S/N): ").lower()

                                    if informatio_view == "s":
                                        frontend_extra.course_information_show(locals()[course_name])
                                        break
                                    elif informatio_view == "n":
                                        break
                                        
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El curso \"{locals()[course_name].course_name}\" no se creara.{TextFormat.CLEAR}")
                                
                                frontend_extra.del_instance_in_class(locals()[course_name])
                                del locals()[course_name]
                                break

                    elif selected_submenu1 == "o":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Profesor{TextFormat.CLEAR}")

                        teacher_name = frontend_extra.name_check_no_numbers("profesor") 
                        locals()[teacher_name] = Person.create_person("Teacher")
                        
                        locals()[teacher_name].name = teacher_name

                        frontend_extra.name_check_no_numbers(locals()[teacher_name], False, "last_name")

                        frontend_extra.set_change_attr_number(locals()[teacher_name], False, "identification")

                        frontend_extra.name_check_without_instance(locals()[teacher_name], False, "address")

                        frontend_extra.set_change_attr_number(locals()[teacher_name], False, "phone_number")
                        
                        frontend_extra.set_change_date(locals()[teacher_name], False, "date_birth")

                        frontend_extra.set_change_age(locals()[teacher_name])

                        frontend_extra.name_check_without_instance(locals()[teacher_name], False, "email")

                        frontend_extra.max_courses_check(locals()[teacher_name])

                        frontend_extra.min_courses_check(locals()[teacher_name])

                        if len(Teacher_type.instances) > 0:
                            while True:
                                set_check = input(f"\nDesea establecer en este momento el tipo de profesor que sera \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" (S/N): ").lower()
                                if set_check == "s":

                                    frontend_extra.view_each_instance(Teacher_type.instances[0])
                                    
                                    teacher_type_name = frontend_extra.name_check_non_existence("tipo de profesor")
                                    locals()[teacher_name].teacher_type = teacher_type_name
                                    
                                    break
                                elif set_check == "n":

                                    break      

                        if len(Turn.instances) > 0:
                            while True:
                                set_check = input(f"\nDesea establecer en este momento el turno del profesor (S/N): ").lower()
                                if set_check == "s":

                                    frontend_extra.view_each_instance(Turn.instances[0])
                                    
                                    turn_name = frontend_extra.name_check_non_existence("turno")
                                    locals()[teacher_name].teacher_type = turn_name
                                    
                                    break
                                elif set_check == "n":

                                    break   

                        while True:
                            verification = input(f"\nDesea crear al profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id: {locals()[teacher_name].id_teacher}, usando la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}El profesor de nombre \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id: {locals()[teacher_name].id_teacher} ha sido creado exitosamente.{TextFormat.CLEAR}")

                                while True:
                                    informatio_view = input(f"\nDeseea ver la información del profesor (S/N): ").lower()

                                    if informatio_view == "s":
                                        frontend_extra.person_information_show(locals()[teacher_name])
                                        break
                                    elif informatio_view == "n":
                                        break
                                        
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El profesor de nombre \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id: {locals()[teacher_name].id_teacher} no sera creaado.{TextFormat.CLEAR}")
                                
                                frontend_extra.del_instance_in_class(locals()[teacher_name])
                                del locals()[teacher_name]
                                break

                    elif selected_submenu1 == "s":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Estudiante{TextFormat.CLEAR}")

                        student_name = frontend_extra.name_check_no_numbers("estudiante") 
                        locals()[student_name] = Person.create_person("Student")

                        locals()[student_name].name = student_name
                        
                        frontend_extra.name_check_no_numbers(locals()[student_name], False, "last_name")

                        frontend_extra.set_change_attr_number(locals()[student_name], False, "identification")

                        frontend_extra.name_check_without_instance(locals()[student_name], False, "address")

                        frontend_extra.set_change_attr_number(locals()[student_name], False, "phone_number")
                        
                        frontend_extra.set_change_date(locals()[student_name], False, "date_birth")

                        frontend_extra.set_change_age(locals()[student_name])

                        frontend_extra.name_check_without_instance(locals()[student_name], False, "email")

                        frontend_extra.max_courses_check(locals()[student_name])

                        frontend_extra.min_courses_check(locals()[student_name])

                        while True:
                            verification = input(f"\nDesea crear al estudiante \"{locals()[student_name].name} {locals()[student_name].last_name}\" con id: {locals()[student_name].id_student}, usando la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}El estudiante de nombre \"{locals()[student_name].name} {locals()[student_name].last_name}\" con id: {locals()[student_name].id_student} ha sido creado exitosamente.{TextFormat.CLEAR}")

                                while True:
                                    informatio_view = input(f"\nDeseea ver la información del estudiante (S/N): ").lower()

                                    if informatio_view == "s":
                                        frontend_extra.person_information_show(locals()[student_name])
                                        break
                                    elif informatio_view == "n":
                                        break
                                        
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El estudiante de nombre \"{locals()[student_name].name} {locals()[student_name].last_name}\" con id: {locals()[student_name].id_student} no sera creaado.{TextFormat.CLEAR}")
                                
                                frontend_extra.del_instance_in_class(locals()[student_name])
                                del locals()[student_name]
                                break

                    input("\nPulse enter para continuar.")          
                    clear_flag()
                
                elif selected_submenu2 == "a":
                    if selected_submenu1 == "m":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar a Matricula{TextFormat.CLEAR}")

                    elif selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar Cursos a Programas{TextFormat.CLEAR}")
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")

                        elif len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")

                        elif not (frontend_extra.programs_availability()):
                            print("\nTodos los programas creados ya alcanzaron su cuota máxima de cursos establecida.")

                        elif not (frontend_extra.courses_availability()):
                            print("\nTodos los cursos creados ya estan agregados a un programa.")
                        
                        else:
                            print(f"\nSeleccione un Programa")

                            frontend_extra.view_each_instance(Program.instances[0], "courses", "max_courses", 1)

                            program_check = frontend_extra.add_requirements_check(Course.instances[0], "programa", "courses", "max_courses")

                            if program_check[0]:
                                print("\nSeleccione un Curso")

                                frontend_extra.view_each_instance(Course.instances[0], "No Establecido", "program", 2)                                
                                
                                while True:
                                    course_name = frontend_extra.name_check_non_existence("curso")

                                    if program_check[1].add_course(locals()[course_name]):
                                        locals()[course_name].program = program_check[1]
                                        break
                     
                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar a Cursos{TextFormat.CLEAR}")
                        if len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")
                        else:
                            print("\nSeleccione un Curso")
                            
                            frontend_extra.view_each_instance(Course.instances[0])
                            course_name = frontend_extra.name_check_non_existence("curso")        

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Agregar al Curso \"{locals()[course_name].course_name}\"\n{TextFormat.CLEAR}"
                                f"[P] Agregar el Curso a un {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rograma\n"
                                f"[F] Agregar Pro{TextFormat.BOLD_UNDERLINE}f{TextFormat.CLEAR}esor al Curso\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "pf" and selected_submenu3 != "":    
                                if selected_submenu3 == "p": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Agregar el Curso \"{locals()[course_name].course_name}\" a un Programa{TextFormat.CLEAR}")
                                    
                                    if len(Program.instances) == 0:
                                        print("\nNo existe ningún programa creado.")

                                    elif not (frontend_extra.programs_availability()):
                                        print("\nTodos los programas creados ya alcanzaron su cuota máxima de cursos establecida.")

                                    elif not (frontend_extra.courses_availability()):
                                        print("\nTodos los cursos creados ya estan agregados a un programa.")

                                    elif locals()[course_name].program != "No Establecido":

                                        print(f"\nEl curso \"{locals()[course_name].course_name}\" se encuentra agregado al programa \"{locals()[course_name].program.program_name}\".")

                                    else:

                                        print(f"\nSeleccione un Programa")

                                        frontend_extra.view_each_instance(Program.instances[0], "courses", "max_courses", 1)

                                        program_check = frontend_extra.add_requirements_check(Course.instances[0], "programa", "courses", "max_courses")

                                        if program_check[0]:
                                            while True:
                                                if program_check[1].add_course(locals()[course_name]):
                                                    locals()[course_name].program = program_check[1]
                                                    break

                                elif selected_submenu3 == "f": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Agregar un Profesor al Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    if len(Person.instances_teacher) == 0:
                                        print("\nNo existe ningún profesor creado.")

                                    elif not (frontend_extra.teachers_availability()):
                                        print("\nTodos los profesores han alcanzado la cantidad máxima de cursos que pueden impartir.")

                                    elif locals()[course_name].teacher != "No Establecido":
                                        print(f"\nEl curso \"{locals()[course_name].course_name}\" ya tiene agregado un profesor.")

                                    else:

                                        print(f"\nSeleccione un Profesor")

                                        frontend_extra.view_each_instance(Person.instances_teacher[0], "courses", "max_courses", 1)

                                        teacher_check = frontend_extra.add_requirements_check(Course.instances[0], "profesor", "courses", "max_courses")

                                        if teacher_check[0]:
                                            while True:
                                                locals()[course_name].teacher = teacher_check[1]
                                                if locals()[course_name].teacher != "No Establecido":
                                                    teacher_check[1].courses = locals()[course_name]
                                                    break   

                    elif selected_submenu1 == "o":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar a Profesores{TextFormat.CLEAR}")
                        if len(Person.instances_teacher) == 0:
                            print("\nNo existe ningún profesor creado.")
                        else:
                            print("\nSeleccione un Profesor")
                            
                            frontend_extra.view_each_instance(Person.instances_teacher[0])
                            teacher_name = frontend_extra.id_check("profesor")

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Agregar al Profesor \"{locals()[teacher_name].name}\"\n{TextFormat.CLEAR}"
                                f"[T] Agregar {TextFormat.BOLD_UNDERLINE}T{TextFormat.CLEAR}ipo de Profesor al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[U] Agregar T{TextFormat.BOLD_UNDERLINE}u{TextFormat.CLEAR}rno al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[C] Agregar un {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}urso al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "tuc" and selected_submenu3 != "":    
                                if selected_submenu3 == "t": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Agregar Tipo de Profesor al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")
                                    
                                    if not (frontend_extra.teachers_availability(2)):
                                        print("\nTodos los profesores ya tienen asignado el tipo de profesor que son.")                                    
                                    
                                    elif locals()[teacher_name].teacher_type != "No Establecido":
                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id: \"{locals()[teacher_name].id_teacher}\" ya esta establecido como profesor de tipo \"{locals()[teacher_name].teacher_type.type_teacher}\".")

                                    else:

                                        print(f"\nSeleccione un Tipo de Profesor")

                                        frontend_extra.view_each_instance(Teacher_type.instances[0])
                                        
                                        type_teacher_check = frontend_extra.name_check_non_existence("tipo de profesor")
                                        locals()[teacher_name].teacher_type = locals()[type_teacher_check]

                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" fue agregado a los profesores de tipo \"{locals()[teacher_name].teacher_type.type_teacher}\".")

                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Agregar Turno al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")
                                    
                                    if not (frontend_extra.teachers_availability(3)):
                                        print("\nTodos los profesores ya tienen asignado un turno.")   

                                    elif locals()[teacher_name].turn != "No Establecido":
                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" ya esta agregado a un turno, el cual es: \"{locals()[teacher_name].turn.turn}\".")
                                    
                                    else:
                                        print(f"\nSeleccione un Turno")

                                        frontend_extra.view_each_instance(Turn.instances[0])
                                        
                                        turn_check = frontend_extra.name_check_non_existence("turno")
                                        locals()[teacher_name].turn = locals()[turn_check]

                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" fue agregado al turno \"{locals()[teacher_name].turn.turn}\"")

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Agregar un Curso al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")

                                    if not (frontend_extra.courses_availability(2)):
                                        print("\nTodos los cursos creados ya tienen agregado un profesor.")

                                    elif len(locals()[teacher_name].courses) >= locals()[teacher_name].max_courses:
                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" ya ha alcanzado previamente la cantidad máxima de curos que puede impartir.")

                                    else:
                                        print(f"\nSeleccione un Curso")

                                        frontend_extra.view_each_instance(Course.instances[0], "No Establecido", "teacher", 2)

                                        course_check = frontend_extra.add_requirements_check(Course.instances[0], "curso", "teacher", "No Establecido", 2)

                                        locals()[teacher_name].courses = course_check[1]
                                        course_check[1].teacher = locals()[teacher_name]

                    elif selected_submenu1 == "s":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar a Estudiantes{TextFormat.CLEAR}")

                        print("\nToda acción de agregar algo a un estudiante, se debe realizar desde la matrícula.")

                    input("\nPresione enter para continuar.")
                    clear_flag()
                
                elif selected_submenu2 == "o":
                    if selected_submenu1 == "m":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Matricula{TextFormat.CLEAR}") 

                    elif selected_submenu1 == "e":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Edificios{TextFormat.CLEAR}") 
                        if len(Building.instances) == 0:
                            print("\nNo existe ningún edificio creado.")
                        else: 

                            frontend_extra.view_each_instance(Building.instances[0])
                            building_name = frontend_extra.name_check_non_existence("edificio")

                            frontend_extra.building_information_show(locals()[building_name])                        

                    elif selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Programas{TextFormat.CLEAR}") 
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")
                        else: 

                            frontend_extra.view_each_instance(Program.instances[0])
                            program_name = frontend_extra.name_check_non_existence("programa")

                            frontend_extra.program_information_show(locals()[program_name])

                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Cursos{TextFormat.CLEAR}") 
                        if len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")
                        else: 
                            
                            frontend_extra.view_each_instance(Course.instances[0])                                
                            course_name = frontend_extra.name_check_non_existence("curso")

                            frontend_extra.course_information_show(locals()[course_name])

                    elif selected_submenu1 == "o":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Profesores{TextFormat.CLEAR}") 
                        if len(Person.instances_teacher) == 0:
                            print("\nNo existe ningún profesor creado.")
                        else: 
                            
                            frontend_extra.view_each_instance(Person.instances_teacher[0])                                
                            teacher_name = frontend_extra.id_check("profesor")

                            frontend_extra.person_information_show(locals()[teacher_name])

                    elif selected_submenu1 == "s":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Estudiantes{TextFormat.CLEAR}") 
                        if len(Person.instances_student) == 0:
                            print("\nNo existe ningún estudiante creado.")
                        else: 
                            
                            frontend_extra.view_each_instance(Person.instances_student[0])                                
                            student_name = frontend_extra.id_check("estudiante")

                            frontend_extra.person_information_show(locals()[student_name])

                    input("\nPulse enter para continuar.")
                    clear_flag()

                elif selected_submenu2 == "m":
                    if selected_submenu1 == "m":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Matricula{TextFormat.CLEAR}")

                    elif selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Programas{TextFormat.CLEAR}")
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")
                        else:

                            frontend_extra.view_each_instance(Program.instances[0])
                            program_name = frontend_extra.name_check_non_existence("programa")        

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información del Programa \"{locals()[program_name].program_name}\"\n{TextFormat.CLEAR}"
                                f"[P] Modificar Nombre del {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rograma\n"
                                f"[D] Modificar Nombre del {TextFormat.BOLD_UNDERLINE}D{TextFormat.CLEAR}irector\n"
                                f"[E] Modificar Cantidad Máxima de {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}studiantes\n"
                                f"[S] Modificar Cantidad Mínima de E{TextFormat.BOLD_UNDERLINE}s{TextFormat.CLEAR}tudiantes\n"
                                f"[C] Modificar Cantidad Máxima de {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}ursos\n"
                                f"[U] Modificar Cantidad Mínima de C{TextFormat.BOLD_UNDERLINE}u{TextFormat.CLEAR}rsos\n"
                                f"[G] Modificar Duración del Pro{TextFormat.BOLD_UNDERLINE}g{TextFormat.CLEAR}rama en años\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "pdescug" and selected_submenu3 != "":    
                                if selected_submenu3 == "p": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_program_name = frontend_extra.name_check_with_numbers("programa", True)

                                    change_name = frontend_extra.change_instance_name(locals()[program_name], new_program_name)
                                    
                                    if change_name[0]:
                                        locals()[new_program_name] = change_name[1]
                                        del locals()[program_name]

                                elif selected_submenu3 == "d": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Director del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_no_numbers(locals()[program_name], True, "principal")

                                elif selected_submenu3 == "e": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    frontend_extra.max_students_check(locals()[program_name], True)  

                                elif selected_submenu3 == "s": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    frontend_extra.min_students_check(locals()[program_name], True)   

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_max_courses = frontend_extra.max_courses_check(locals()[program_name], True) 

                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_min_courses = frontend_extra.min_courses_check(locals()[program_name], True)

                                elif selected_submenu3 == "g": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Duración del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_program_durations = frontend_extra.program_duration_check(locals()[program_name], True)   

                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Cursos{TextFormat.CLEAR}")
                        if len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Course.instances[0])
                            course_name = frontend_extra.name_check_non_existence("curso")        

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información del Curso \"{locals()[course_name].course_name}\"\n{TextFormat.CLEAR}"
                                f"[N] Modificar {TextFormat.BOLD_UNDERLINE}N{TextFormat.CLEAR}onmbre del Curso\n"
                                f"[C] Modificar {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}reditos del Curso\n"
                                f"[H] Modificar {TextFormat.BOLD_UNDERLINE}H{TextFormat.CLEAR}oras Semanales del Curso\n"
                                f"[P] Modificar {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}recio del Curso\n"
                                f"[A] Modificar Cantidad Máxima de {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}lumnos del Curso\n"
                                f"[L] Modificar Cantidad Mínima de A{TextFormat.BOLD_UNDERLINE}l{TextFormat.CLEAR}umnos del Curso\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "nchpal" and selected_submenu3 != "":    
                                if selected_submenu3 == "n": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")

                                    new_course_name = frontend_extra.name_check_with_numbers("curso", True)

                                    change_name = frontend_extra.change_instance_name(locals()[course_name], new_course_name)
                                    
                                    if change_name[0]:
                                        locals()[new_course_name] = change_name[1]
                                        del locals()[course_name]

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Creditos del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[course_name], True, "credits")

                                elif selected_submenu3 == "h": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Horas Semanales del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[course_name], True, "week_hours")
 
                                elif selected_submenu3 == "p": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Precio del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[course_name], True, "price")

                                elif selected_submenu3 == "a": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Alumnos del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.max_students_check(locals()[course_name], True)

                                elif selected_submenu3 == "l": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Alumnos del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.min_students_check(locals()[course_name], True)

                    elif selected_submenu1 == "o":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Profesores{TextFormat.CLEAR}")
                        if len(Person.instances_teacher) == 0:
                            print("\nNo existe ningún profesor creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Person.instances_teacher[0])
                            teacher_name = frontend_extra.id_check("profesor")        

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información del Profesor \"{locals()[teacher_name].name}\"\n{TextFormat.CLEAR}"
                                f"[N] Modificar {TextFormat.BOLD_UNDERLINE}N{TextFormat.CLEAR}onmbre del Profesor\n"
                                f"[A] Modificar {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}pellido del Profesor\n"
                                f"[C] Modificar {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}édula del Profesor\n"
                                f"[D] Modificar {TextFormat.BOLD_UNDERLINE}D{TextFormat.CLEAR}irección del Profesor\n"
                                f"[U] Modificar N{TextFormat.BOLD_UNDERLINE}ú{TextFormat.CLEAR}mero Telefónico del Profesor\n"
                                f"[F] Modificar {TextFormat.BOLD_UNDERLINE}F{TextFormat.CLEAR}echa de Nacimiento (Edad) del Profesor\n"
                                f"[E] Modificar {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}mail del Profesor\n"
                                f"[M] Modificar Cantidad {TextFormat.BOLD_UNDERLINE}M{TextFormat.CLEAR}áxima de Curso del Profesor\n"
                                f"[I] Modificar Cantidad M{TextFormat.BOLD_UNDERLINE}í{TextFormat.CLEAR}nima de Curso del Profesor\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "nacdufemi" and selected_submenu3 != "":    
                                if selected_submenu3 == "n": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")

                                    new_teacher_name = frontend_extra.name_check_no_numbers("profesor", True)

                                    change_name = frontend_extra.change_instance_name(locals()[teacher_name], new_teacher_name)
                                    
                                    if change_name[0]:
                                        locals()[new_teacher_name] = change_name[1]
                                        del locals()[teacher_name]

                                elif selected_submenu3 == "a": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Apellido del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_no_numbers(locals()[teacher_name], True, "last_name")

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cédula del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[teacher_name], True, "identification")

                                elif selected_submenu3 == "d": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Dirección del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_without_instance(locals()[teacher_name], True, "address")

                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Número Telefónico del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[teacher_name], True, "phone_number")

                                elif selected_submenu3 == "f": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Fecha de Nacimiento (Edad) del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_date(locals()[teacher_name], True, "date_birth")
                                    frontend_extra.set_change_age(locals()[teacher_name])

                                elif selected_submenu3 == "e": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Email del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_without_instance(locals()[teacher_name], True, "email")

                                elif selected_submenu3 == "m": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Cursos del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.max_courses_check(locals()[teacher_name], True)

                                elif selected_submenu3 == "i": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Cursos del Profesor \"{locals()[teacher_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.min_courses_check(locals()[teacher_name], True)

                    elif selected_submenu1 == "s":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Estudiantes{TextFormat.CLEAR}")
                        if len(Person.instances_student) == 0:
                            print("\nNo existe ningún estudiante creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Person.instances_student[0])
                            student_name = frontend_extra.id_check("estudiante")        

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información del Estudiante \"{locals()[student_name].name}\"\n{TextFormat.CLEAR}"
                                f"[N] Modificar {TextFormat.BOLD_UNDERLINE}N{TextFormat.CLEAR}onmbre del Estudiante\n"
                                f"[A] Modificar {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}pellido del Estudiante\n"
                                f"[C] Modificar {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}édula del Estudiante\n"
                                f"[D] Modificar {TextFormat.BOLD_UNDERLINE}D{TextFormat.CLEAR}irección del Estudiante\n"
                                f"[U] Modificar N{TextFormat.BOLD_UNDERLINE}ú{TextFormat.CLEAR}mero Telefónico del Estudiante\n"
                                f"[F] Modificar {TextFormat.BOLD_UNDERLINE}F{TextFormat.CLEAR}echa de Nacimiento (Edad) del Estudiante\n"
                                f"[E] Modificar {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}mail del Estudiante\n"
                                f"[M] Modificar Cantidad {TextFormat.BOLD_UNDERLINE}M{TextFormat.CLEAR}áxima de Cursos del Estudiante\n"
                                f"[I] Modificar Cantidad M{TextFormat.BOLD_UNDERLINE}í{TextFormat.CLEAR}nima de Cursos del Estudiante\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "nacdufemi" and selected_submenu3 != "":    
                                if selected_submenu3 == "n": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")

                                    new_student_name = frontend_extra.name_check_no_numbers("estudiante", True)

                                    change_name = frontend_extra.change_instance_name(locals()[student_name], new_student_name)
                                    
                                    if change_name[0]:
                                        locals()[new_student_name] = change_name[1]
                                        del locals()[student_name]

                                elif selected_submenu3 == "a": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Apellido del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_no_numbers(locals()[student_name], True, "last_name")

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cédula del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[student_name], True, "identification")

                                elif selected_submenu3 == "d": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Dirección del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_without_instance(locals()[student_name], True, "address")

                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Número Telefónico del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_attr_number(locals()[student_name], True, "phone_number")

                                elif selected_submenu3 == "f": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Fecha de Nacimiento (Edad) del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.set_change_date(locals()[student_name], True, "date_birth")
                                    frontend_extra.set_change_age(locals()[student_name])

                                elif selected_submenu3 == "e": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Email del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_without_instance(locals()[student_name], True, "email")

                                elif selected_submenu3 == "m": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Cursos del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.max_courses_check(locals()[student_name], True)

                                elif selected_submenu3 == "i": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Cursos del Estudiante \"{locals()[student_name].name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.min_courses_check(locals()[student_name], True)

                    input("\nPulse enter para continuar.")          
                    clear_flag()

                elif selected_submenu2 == "e":
                    if selected_submenu1 == "m":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Matricula{TextFormat.CLEAR}") 

                    elif selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programas{TextFormat.CLEAR}") 
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Program.instances[0])
                            program_name = frontend_extra.name_check_non_existence("programa")

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programa \"{locals()[program_name].program_name}\"\n{TextFormat.CLEAR}"
                                f"\n[P] Eliminar el {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rograma \"{locals()[program_name].program_name}\"\n"
                                f"[C] Eliminar {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}ursos del Programa \"{locals()[program_name].program_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            if selected_submenu3 in "pcr" and selected_submenu3 != "":     
                                if selected_submenu3 == "p":      
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Eliminar Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")                                                                  
                                    while True:
                                        review_information = input(f"\nDesea revisar la información asociada al programa \"{locals()[program_name].program_name}\" antes de elimninarlo (S/N): ").lower()
                                        if review_information == "s":

                                            frontend_extra.program_information_show(locals()[program_name])
                                            break
                                        elif review_information == "n":
                                            break

                                    while True:
                                        print(f"\n{TextFormat.RED}La acción de eliminación no puede ser revertida, tenga cuidado con los programas que elimina.{TextFormat.CLEAR}")
                                        delete_check = input(f"\nConfirme eliminación del programa \"{locals()[program_name].program_name}\" (S/N): ").lower()
                                        if delete_check == "s":

                                            if len(locals()[program_name].courses) > 0: 
                                                frontend_extra.set_attribute_in_list_in_instance(locals()[program_name], "courses", "program", "No Establecido") 
                                            
                                            frontend_extra.del_instance_in_class(locals()[program_name])                                          
                                            
                                            del locals()[program_name]               

                                            print(f"\nEl programa de nombre \"{program_name}\" fue eliminado exitosamente.")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo ninguna acción, el programa de nombre \"{locals()[program_name].program_name}\" no fue eliminado.")
                                            break

                                elif selected_submenu3 == "c":  
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Eliminar Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    if len(locals()[program_name].courses) == 0:
                                        print(f"\nEl programa \"{locals()[program_name].program_name}\" no tiene cursos agregados.")                         
                                    else:
                                                
                                        frontend_extra.view_each_instance(locals()[program_name], "courses", "course_name", 3)                                    
                                        
                                        print("\nEliminar curso.")

                                        course_name = frontend_extra.name_check_non_existence("curso")

                                        while True:
                                            delete_check = input(f"\nConfirme eliminación del curso \"{locals()[course_name].course_name}\" del programa \"{locals()[program_name].program_name}\" (S/N): ").lower()
                                            if delete_check == "s":
                                                locals()[program_name].del_course(locals()[course_name])
                                                break
                                            elif delete_check == "n":
                                                print(f"\nNo se realizo ninguna acción, el curso de nombre \"{locals()[course_name].course_name}\" no fue eliminado del programa \"{locals()[program_name].program_name}\".")
                                                break                               

                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Cursos{TextFormat.CLEAR}") 
                        if len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Course.instances[0])
                            course_name = frontend_extra.name_check_non_existence("curso")

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Curso \"{locals()[course_name].course_name}\"\n{TextFormat.CLEAR}"
                                f"\n[C] Eliminar el {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}urso \"{locals()[course_name].course_name}\"\n"
                                f"[P] Eliminar el {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rograma del Curso \"{locals()[course_name].course_name}\"\n"
                                f"[F] Eliminar el Pro{TextFormat.BOLD_UNDERLINE}f{TextFormat.CLEAR}esor del Curso \"{locals()[course_name].course_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            clear_screen()
                            if selected_submenu3 in "cpf" and selected_submenu3 != "":     
                                if selected_submenu3 == "c":
                                    print(f"\n{TextFormat.CYAN}Eliminar Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")                                                                  
                                    while True:
                                        review_information = input(f"\nDesea revisar la información asociada al curso \"{locals()[course_name].course_name}\" antes de elimninarlo (S/N): ").lower()
                                        if review_information == "s":

                                            frontend_extra.course_information_show(locals()[course_name])
                                            break
                                        elif review_information == "n":
                                            break

                                    while True:
                                        print(f"\n{TextFormat.RED}La acción de eliminación no puede ser revertida, tenga cuidado con los cursos que elimina.{TextFormat.CLEAR}")
                                        delete_check = input(f"\nConfirme eliminación del curso \"{locals()[course_name].course_name}\" (S/N): ").lower()
                                        if delete_check == "s":
                                            if locals()[course_name].program != "No Establecido":
                                                frontend_extra.del_instance_in_other_instance_list(locals()[course_name], "program", "courses")                                            
                                            
                                            if locals()[course_name].teacher != "No Establecido":
                                                frontend_extra.del_instance_in_other_instance_list(locals()[course_name], "teacher", "courses")
                                            
                                            frontend_extra.del_instance_in_class(locals()[course_name])
                                            del locals()[course_name]              

                                            print(f"\nEl curso de nombre \"{course_name}\" fue eliminado exitosamente.")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo ninguna acción, el curso de nombre \"{locals()[course_name].course_name}\" no fue eliminado.")
                                            break

                                elif selected_submenu3 == "p":
                                    print(f"\n{TextFormat.CYAN}Eliminar Programa del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")                                                                  
                                    if len(Program.instances) == 0:
                                        print("\nNo existe ningún programa creado.")
                                    elif locals()[course_name].program == "No Establecido":
                                        print(f"\nEl curso \"{locals()[course_name].course_name}\" no tiene ningún programa asignado.")
                                    else:
                                        print("\nEliminar programa.")
                                        while True:
                                            delete_check = input(f"\nConfirme eliminación del programa \"{locals()[course_name].program.program_name}\" del curso \"{locals()[course_name].course_name}\" (S/N): ").lower()
                                            if delete_check == "s":
                                                frontend_extra.del_instance_in_other_instance_list(locals()[course_name], "program","courses")
                                                locals()[course_name].program = "No Establecido"

                                                print(f"\nPrograma eliminado exitosamente del curso \"{locals()[course_name].course_name}\".")
                                                break
                                            elif delete_check == "n":
                                                print(f"\nNo se realizo ninguna acción, el programa \"{locals()[course_name].program.program_name}\" no fue eliminado del curso \"{locals()[course_name].course_name}\".")
                                                break

                                elif selected_submenu3 == "f":
                                    print(f"\n{TextFormat.CYAN}Eliminar Profesor del Curso \"{locals()[course_name].course_name}\"{TextFormat.CLEAR}")                                                                  
                                    if len(Person.instances_teacher) == 0:
                                        print("\nNo existe ningún profesor creado.")
                                    elif locals()[course_name].teacher == "No Establecido":
                                        print(f"\nEl curso \"{locals()[course_name].course_name}\" no tiene ningún profesor asignado.")
                                    else:
                                        print("\nEliminar profesor.")
                                        while True:
                                            delete_check = input(f"\nConfirme eliminación del profesor \"{locals()[course_name].teacher.name} {locals()[course_name].teacher.last_name}\" con id: \"{locals()[course_name].teacher.id_teacher}\" del curso \"{locals()[course_name].course_name}\" (S/N): ").lower()
                                            if delete_check == "s":
                                                frontend_extra.del_instance_in_other_instance_list(locals()[course_name], "teacher","courses")
                                                locals()[course_name].teacher = "No Establecido"
                                                print(f"\nProfesor eliminado existosamente del curso \"{locals()[course_name].course_name}\".")
                                                break
                                            elif delete_check == "n":
                                                print(f"\nNo se realizo ninguna acción, el profesor \"{locals()[course_name].teacher.name} {locals()[course_name].teacher.last_name}\" con id: \"{locals()[course_name].teacher.id_teacher}\" no fue eliminado del curso \"{locals()[course_name].course_name}\".")
                                                break

                    elif selected_submenu1 == "o":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Profesores{TextFormat.CLEAR}") 
                        if len(Person.instances_teacher) == 0:
                            print("\nNo existe ningún profesor creado.")
                        else:
                            
                            frontend_extra.view_each_instance(Person.instances_teacher[0])
                            teacher_name = frontend_extra.id_check("profesor")

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n{TextFormat.CLEAR}"
                                f"\n[P] Eliminar al {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rofesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[T] Eliminar el {TextFormat.BOLD_UNDERLINE}T{TextFormat.CLEAR}ipo de Profesor al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[U] Eliminar el T{TextFormat.BOLD_UNDERLINE}u{TextFormat.CLEAR}rno al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[C] Eliminar un {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}urso al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            clear_screen()
                            if selected_submenu3 in "ptuc" and selected_submenu3 != "":     
                                if selected_submenu3 == "p":
                                    print(f"\n{TextFormat.CYAN}Eliminar Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")                                                                  
                                    while True:
                                        review_information = input(f"\nDesea revisar la información asociada al profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" antes de elimninarlo (S/N): ").lower()
                                        if review_information == "s":

                                            frontend_extra.person_information_show(locals()[teacher_name])
                                            break
                                        elif review_information == "n":
                                            break

                                    while True:
                                        print(f"\n{TextFormat.RED}La acción de eliminación no puede ser revertida, tenga cuidado con los profesores que elimina.{TextFormat.CLEAR}")
                                        delete_check = input(f"\nConfirme eliminación del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" (S/N): ").lower()
                                        if delete_check == "s":


                                            if len(locals()[teacher_name].courses) > 0: 
                                                frontend_extra.set_attribute_in_list_in_instance(locals()[teacher_name], "courses", "teacher", "No Establecido") 
                                            
                                            frontend_extra.del_instance_in_class(locals()[teacher_name])                                          
                                            
                                            del locals()[teacher_name]      

                                            print(f"\nEl profesor fue eliminado exitosamente.")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo ninguna acción, el profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" no fue eliminado.")
                                            break

                                elif selected_submenu3 == "t":
                                    print(f"\n{TextFormat.CYAN}Eliminar el Tipo de Profesor al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")                                                                  
                                
                                    while True:
                                        delete_check = input(f"\nConfirme eliminación del tipo de profesor \"{locals()[teacher_name].teacher_type.teacher_type}\" del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" (S/N): ").lower()
                                        if delete_check == "s":
                                            locals()[teacher_name].teacher_type = "No Establecido"

                                            print(f"\nEl tipo de profesor fue eliminado exitosamente del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\".")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo ninguna acción, el profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" sigue siendo de tipo \"{locals()[teacher_name].teacher_type.teacher_type}\".")
                                            break                                   
                                
                                elif selected_submenu3 == "u":
                                    print(f"\n{TextFormat.CYAN}Eliminar el Turno al Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")                                                                  
                                
                                    while True:
                                        delete_check = input(f"\nConfirme eliminación del turno \"{locals()[teacher_name].turn.turn}\" del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" (S/N): ").lower()
                                        if delete_check == "s":
                                            locals()[teacher_name].turn = "No Establecido"

                                            print(f"\nEl turno fue eliminado exitosamente del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\".")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo ninguna acción, el profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" sigue en el turno \"{locals()[teacher_name].turn.turn}\".")
                                            break    

                                elif selected_submenu3 == "c":
                                    print(f"\n{TextFormat.CYAN}Eliminar Curso del Profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\"{TextFormat.CLEAR}")                                                                  

                                    if len(locals()[teacher_name].courses) == 0:
                                        print(f"\nEl profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" no tiene cursos agregados.")                         
                                    else:
                                                
                                        frontend_extra.view_each_instance(locals()[teacher_name], "courses", "course_name", 3)                                    
                                        
                                        print("\nEliminar curso.")

                                        course_name = frontend_extra.name_check_non_existence("curso")

                                        while True:
                                            delete_check = input(f"\nConfirme eliminación del curso \"{locals()[course_name].course_name}\" del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\" (S/N): ").lower()
                                            if delete_check == "s":
                                                
                                                locals()[course_name].teacher = "No Establecido"

                                                for i in locals()[teacher_name].courses:
                                                    if i == locals()[course_name]:
                                                        index = locals()[teacher_name].courses.index(i)
                                                        del locals()[teacher_name].courses[index]
                                                
                                                print(f"\nCurso \"{locals()[course_name].course_name}\" elimiando exitosamente del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\".")                                                

                                                break

                                            elif delete_check == "n":
                                                print(f"\nNo se realizo ninguna acción, el curso de nombre \"{locals()[course_name].course_name}\" no fue eliminado del profesor \"{locals()[teacher_name].name} {locals()[teacher_name].last_name}\" con id \"{locals()[teacher_name].id_teacher}\".")
                                                break    

                    elif selected_submenu1 == "s":
                        pass

                    input("\nPulse enter para continuar.")          
                    clear_flag()

            elif selected_submenu2 == "r":
                clear_flag()

            else:
                invalid_selection()

        elif selected_submenu1 == "r":
            clear_flag()

        else:
            invalid_selection()

    elif selected_menu == "v":
        pass
        clear_flag()

    elif selected_menu == "c":
        clear_screen()
        print(f"{TextFormat.CYAN}\nSub Menú - Calcular Analítica{TextFormat.CLEAR}\n"
              "[P] Por programa\n"
              "[D] Por estudiante\n"
              "[R] Regresar al Menú Principal\n")
        selected_submenu1 = input("Digite una opción: ").lower()
        if selected_submenu1 == "p":
            pass
            clear_flag()
        elif selected_submenu1 == "d":
            pass
            clear_flag()
        elif selected_submenu1 == "r":
            clear_flag()
        else:
            invalid_selection()

    elif selected_menu == "s":
        selected_menu = input(f"{TextFormat.YELLOW}\nDigite \"S\", si está seguro que desea salir del programa "
                              f"(Tomar en cuenta que esto borrara toda la información creada): "
                              f"{TextFormat.CLEAR}").lower()
        if selected_menu != "s":
            invalid_selection()
        else:
            clear_screen()

    else:
        invalid_selection()
