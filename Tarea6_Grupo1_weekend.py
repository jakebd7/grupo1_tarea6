__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez, Marco Cordoba'

# ----------------------
# Importación de Módulos
# ----------------------

#import extra_for_test
import copy
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
programa_1.max_courses = 25
programa_1.min_courses = 10
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
print(f"id_profesor: {Juan.id_teacher}")

# Curso Matematica de prueba
matematica = Course("matematica")
matematica.credits = 5
matematica.week_hours = 42
matematica.program = programa_1
matematica.price = 200
matematica.teacher = Juan
matematica.max_students = 20
matematica.min_students = 10


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
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Programa{TextFormat.CLEAR}")
      
                        program_name = frontend_extra.name_check_with_numbers("programa")
                        locals()[program_name] = Program(program_name)

                        frontend_extra.name_check_no_numbers(locals()[program_name], False, "director")  

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
                                        
                                        input("\nPulse enter para continuar.")
                                        break
                                    elif informatio_view == "n":
                                        break

                                clear_flag()
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El programa \"{locals()[program_name].program_name}\" no se creara.{TextFormat.CLEAR}")
                                frontend_extra.del_instance_in_class(locals()[program_name])
                                del locals()[program_name]
                                                                
                                input("\nPulse enter para continuar.")
                                clear_flag()
                                break
                    elif selected_submenu1 == "c":
                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Creación de Nuevo Curso{TextFormat.CLEAR}")

                            course_name = frontend_extra.name_check_with_numbers("curso")                              
                            locals()[course_name] = Course(course_name)

                            frontend_extra.set_change_attr_number(locals()[course_name], False, "credits")

                            frontend_extra.set_change_attr_number(locals()[course_name], False, "week_hours")

                            while True:
                                try:
                                    program_name = input("\nNombre del programa al que pertenecera el curso: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break
                                    
                                    only_underscores = True
                                    for i in program_name:
                                        if i != "_":
                                            only_underscores = False
                                            break
                                        
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")
                                    elif only_underscores == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente guiones bajos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " " and i != "_":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

                                    for instance in Program.instances:
                                        if locals()[program_name] == instance: 
                                            locals()[course_name].program = instance

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\"")
                                else:
                                    break   

                            frontend_extra.set_change_attr_number(locals()[course_name], False, "price")

                            print(f"id_profesor: {Juan.id_teacher}")
                            while True:
                                try:
                                    id_teacher = int(input("\nId del profesor del curso: "))
                                    if id_teacher < 0:
                                        raise SyntaxError("\nLos Id de los profesores no son números negativos.")

                                    teacher_check = False
                                    for instance in Person.instances_teacher:
                                        if id_teacher == instance.id_teacher:                                            
                                            locals()[course_name].teacher = instance
                                            teacher_check = True

                                    if teacher_check == False:      
                                        raise SyntaxError(f"\nNo existe ningún profesor con el id: \"{id_teacher}\".")

                                except ValueError:
                                    print("\nDebe ingresar únicamente números enteros.")
                                except SyntaxError as arg:
                                    print(arg)
                                except KeyError:
                                    print("Entro en Keyerror")
                                    break
                                else:
                                    break
                            
                            frontend_extra.max_students_check(locals()[course_name])

                            frontend_extra.min_students_check(locals()[course_name])

                            while True:
                                verification = input(f"\nDesea crear el curso \"{locals()[course_name].course_name}\" con la información asociada que ha ingresado (S/N): ").lower()
                                if verification == "s":
                                    print(f"\n{TextFormat.CYAN}Se ha creado el curso \"{locals()[course_name].course_name}\" con la siguiente información asociada:\n{TextFormat.CLEAR}"
                                        f"\nNombre del Curso: {locals()[course_name].course_name}\n"
                                        f"Creditos del Curso: {locals()[course_name].credits}\n"
                                        f"Cantidad de Horas Semanales: {locals()[course_name].week_hours}\n"
                                        f"Programa al que Pertenece el Curso: {locals()[course_name].program.program_name}\n"
                                        f"Precio del Curso: {locals()[course_name].price}\n"
                                        f"Profesor del Curso: {locals()[course_name].teacher.name} {locals()[course_name].teacher.last_name}\n"   
                                        f"Id del Profesor: {locals()[course_name].teacher.id_teacher}\n"
                                        f"Máximo de Estudiantes: {locals()[course_name].max_students}\n"
                                        f"Mínimo de Estudiantes: {locals()[course_name].min_students}\n")
                                            
                                    input("Pulse enter para continuar.")
                                    clear_flag()
                                    break
                                elif verification == "n":
                                    print(f"\n{TextFormat.CYAN}El curso \"{locals()[course_name].course_name}\" no se creara.{TextFormat.CLEAR}")
                                    for instance in Course.instances:
                                        if locals()[course_name] == instance:
                                            instance_index = Course.instances.index(instance)
                                            del Course.instances[instance_index]
                                    del locals()[course_name]
                                                                    
                                    input("\nPulse enter para continuar.")
                                    clear_flag()
                                    break
                    clear_flag()
                if selected_submenu2 == "a":
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar Cursos a Programas{TextFormat.CLEAR}")
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        elif len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        else:
                            program_name = str
                            while True:
                                try:
                                    program_name = input("\nIngrese el nombre de un programa: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break

                                    only_underscores = True
                                    for i in program_name:
                                        if i != "_":
                                            only_underscores = False
                                            break
                                    
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")
                                    elif only_underscores == True:                                    
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente guiones bajos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " " and i != "_":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

                                    instance_check = False
                                    for instance in Program.instances:
                                        if locals()[program_name] == instance:
                                            instance_check = True

                                    if instance_check == False:
                                        raise KeyError

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\".")
                                else:
                                    break 

                            curse_not_in_program = False
                            for instance in Course.instances:
                                if not (instance in locals()[program_name].courses):
                                    curse_not_in_program = True
                                    break

                            if curse_not_in_program == False:
                                print(f"\nTodos lo cursos existentes ya estan agregados al programa \"{program_name}\".")
 
                                input("\nPresione enter para continuar.")
                                clear_flag()
                            elif len(locals()[program_name].courses) > locals()[program_name].max_courses:
                                print(f"\nNo se pueden agregar mas cursos al programa \"{locals()[program_name].program_name}\". El programa \"{locals()[program_name].program_name}\" ya ha alcanzado la cantidad máxima de cursos establecida.")
                                
                                input("\nPresione enter para continuar.")
                                clear_flag()
                            else:    
                                course_name = str
                                while True:
                                    try:
                                        course_name = input(f"\nIngrese el nombre del curso que se agregara al programa \"{program_name}\": ")
                                        only_white_spaces = True
                                        for i in course_name:
                                            if i != " ":
                                                only_white_spaces = False
                                                break

                                        only_underscores = True
                                        for i in course_name:
                                            if i != "_":
                                                only_underscores = False
                                                break
                                        
                                        if only_white_spaces == True:
                                            raise ValueError("\nEl nombre del curso no debe contener únicamente espacios vacíos.")
                                        elif only_underscores == True:                                    
                                            raise ValueError("\nEl nombre del curso no debe contener únicamente guiones bajos.")

                                        for i in course_name:
                                            if i.isalnum() == False:
                                                if i != " " and i != "_":                                        
                                                    raise ValueError("\nEl nombre del curso solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

                                        instance_check = False
                                        for instance in Course.instances:
                                            if locals()[course_name] == instance:
                                                instance_check = True

                                        if instance_check == False:
                                            raise KeyError

                                        for instance in locals()[program_name].courses:
                                            if locals()[course_name] in instance:
                                               raise ValueError(f"\nYa existe un curso con el nombre \"{course_name}\" en programa \"{program_name}\"")                                  
                                    
                                    except ValueError as arg:
                                        print(arg)
                                    except KeyError as arg:
                                        print(f"\nNo existe un curso con el nombre \"{course_name}\".")
                                    else:
                                        break 

                                locals()[program_name].add_course(locals()[course_name])
                                
                                input("\nPresione enter para continuar.")
                                clear_flag()
                     
                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Agregar a Cursos{TextFormat.CLEAR}")
                        print("\nLa opción de agregar no esta permitida para los cursos.")

                        input("\nPresione enter para continuar.")
                    
                    
                    clear_flag()
                if selected_submenu2 == "o":
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Programas{TextFormat.CLEAR}") 
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        else: 
                            while True:
                                program_list = input("\nDesea ver una lista de todos los programas creados (S/N): ").lower()
                                if program_list == "s":
                                    print("")
                                    for i in range(0, len(Program.instances),1):
                                        print(f"({i}) {Program.instances[i].program_name}")
                                    break
                                elif program_list == "n":
                                    break

                            program_name = frontend_extra.name_check_non_existence("programa")

                            frontend_extra.program_information_show(locals()[program_name])

                            input("\nPulse enter para continuar.")
                            clear_screen() 

                    elif selected_submenu1 == "c":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Consultar Información de Cursos{TextFormat.CLEAR}") 
                        if len(Course.instances) == 0:
                            print("\nNo existe ningún curso creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        else: 
                            while True:
                                course_list = input("\nDesea ver una lista de todos los cursos creados (S/N): ").lower()
                                if course_list == "s":
                                    print("")
                                    for i in range(0, len(Course.instances),1):
                                        print(f"({i}) {Course.instances[i].course_name}")
                                    break
                                elif course_list == "n":
                                    break
                                
                            course_name = frontend_extra.name_check_non_existence("curso")

                            frontend_extra.course_information_show(locals()[course_name])

                            input("\nPulse enter para continuar.")
                            clear_screen() 

                if selected_submenu2 == "m":
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Información de Programas{TextFormat.CLEAR}")
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        else:
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
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "d": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Director del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")
                                    
                                    frontend_extra.name_check_no_numbers(locals()[program_name], True, "director")
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "e": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    frontend_extra.max_students_check(locals()[program_name], True)                            
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "s": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    frontend_extra.min_students_check(locals()[program_name], True)                               
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_max_courses = frontend_extra.max_courses_check(locals()[program_name], True)                              
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_min_courses = frontend_extra.min_courses_check(locals()[program_name], True)                          
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "g": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Duración del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_program_durations = frontend_extra.program_duration_check(locals()[program_name], True)                              
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                            elif selected_submenu3 == "r":
                                clear_flag()
                            else:
                                invalid_selection()
                    clear_flag()
                if selected_submenu2 == "e":
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programas{TextFormat.CLEAR}") 
                        if len(Program.instances) == 0:
                            print("\nNo existe ningún programa creado.")

                            input("\nPresione enter para continuar.")
                            clear_flag()
                        else:
                            program_name = str
                            while True:
                                try:
                                    program_name = input("\nIngrese el nombre de un programa: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break

                                    only_underscores = True
                                    for i in program_name:
                                        if i != "_":
                                            only_underscores = False
                                            break
                                    
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")
                                    elif only_underscores == True:                                    
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente guiones bajos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " " and i != "_":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

                                    instance_check = False
                                    for instance in Program.instances:
                                        if locals()[program_name] == instance:
                                            instance_check = True

                                    if instance_check == False:
                                        raise KeyError

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\".")
                                else:
                                    break   

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programa \"{locals()[program_name].program_name}\"\n{TextFormat.CLEAR}"
                                f"\n[P] Eliminar el {TextFormat.BOLD_UNDERLINE}P{TextFormat.CLEAR}rograma \"{locals()[program_name].program_name}\"\n"
                                f"[C] Eliminar {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}ursos del Programa \"{locals()[program_name].program_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")
                            if selected_submenu3 in "pcr" and selected_submenu3 != "":     
                                if selected_submenu3 == "p":                                    
                                    while True:
                                        review_information = input(f"\nDesea revisar la información asociada al programa \"{locals()[program_name].program_name}\" antes de elimninarlo (S/N): ").lower()
                                        if review_information == "s":
                                            print(f"\nNombre del Programa: {locals()[program_name].program_name}\n"
                                                  f"Fecha de Creación del Programa: {locals()[program_name].creation_date_program}\n"
                                                  f"Estatus del Programa: {locals()[program_name].program_status}\n"
                                                  f"Director: {locals()[program_name].principal}\n"
                                                  f"Número de Cursos del Programa: {len(locals()[program_name].courses)}\n"
                                                  f"Máximo de Estudiantes: {locals()[program_name].max_students}\n"
                                                  f"Mínimo de Estudiantes: {locals()[program_name].min_students}\n"
                                                  f"Máximo de Cursos: {locals()[program_name].max_courses}\n"
                                                  f"Mínimo de Cursos: {locals()[program_name].min_courses}\n"                            
                                                  f"Duración del Programa en años: {locals()[program_name].program_duration}")
                                            break
                                        elif review_information == "n":
                                            break

                                    while True:
                                        print(f"\n{TextFormat.RED}La acción de eliminación no puede ser revertida, tenga cuidado con los programas que elimina.{TextFormat.CLEAR}")
                                        delete_check = input(f"\nConfirme eliminación del programa \"{locals()[program_name].program_name}\" (S/N): ").lower()
                                        if delete_check == "s":
                                            for instance in Program.instances:
                                                if locals()[program_name] == instance:
                                                    instance_index = Program.instances.index(instance)
                                                    del Program.instances[instance_index]
                                            
                                            del locals()[program_name]               
                                            print(f"\nEl programa de nombre \"{program_name}\" fue eliminado exitosamente.")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo níngun acción, el programa de nombre \"{locals()[program_name].program_name}\" no fue eliminado.")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()

                                elif selected_submenu3 == "c":  
                                    if len(locals()[program_name].courses) == 0:
                                        print(f"\nEl programa \"{locals()[program_name].program_name}\" no tiene cursos agreados.")  
                                        
                                        input("\nPresione enter para continuar.")
                                        clear_flag()                         
                                    else:
                                        while True:
                                            course_list = input("\nDesea ver una lista de todos los cursos del programa (S/N): ").lower()
                                            if course_list == "s":
                                                print("")
                                                for i in range(0, len(Program.instances),1):
                                                    for j in Program.instances[i].courses:
                                                        print(f"({i}) {j.course_name}")
                                                break
                                            elif course_list == "n":
                                                break                                        
                                        
                                        course_name = str
                                        while True:
                                            try:
                                                course_name = input(f"\nIngrese el nombre del curso que se eliminara del programa \"{program_name}\": ")
                                                only_white_spaces = True
                                                for i in course_name:
                                                    if i != " ":
                                                        only_white_spaces = False
                                                        break

                                                only_underscores = True
                                                for i in course_name:
                                                    if i != "_":
                                                        only_underscores = False
                                                        break
                                                
                                                if only_white_spaces == True:
                                                    raise ValueError("\nEl nombre del curso no debe contener únicamente espacios vacíos.")
                                                elif only_underscores == True:                                    
                                                    raise ValueError("\nEl nombre del curso no debe contener únicamente guiones bajos.")

                                                for i in course_name:
                                                    if i.isalnum() == False:
                                                        if i != " " and i != "_":                                        
                                                            raise ValueError("\nEl nombre del curso solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

                                                instance_check = False
                                                for instance in Course.instances:
                                                    if locals()[course_name] == instance:
                                                        instance_check = True

                                                if instance_check == False:
                                                    raise KeyError

                                            except ValueError as arg:
                                                print(arg)
                                            except KeyError:
                                                print(f"\nNo existe un curso con el nombre \"{course_name}\".")
                                            else:
                                                break 

                                        while True:
                                            delete_check = input(f"\nConfirme eliminación del curso \"{locals()[course_name].course_name}\" del programa \"{locals()[program_name].program_name}\" (S/N): ").lower()
                                            if delete_check == "s":
                                                locals()[program_name].del_course(locals()[course_name])

                                                input("\nPresione enter para continuar.")
                                                clear_flag()
                                                break
                                            elif delete_check == "n":
                                                print(f"\nNo se realizo níngun acción, el curso de nombre \"{locals()[course_name].course_name}\" no fue eliminado del programa \"{locals()[program_name].program_name}\".")
                                                
                                                input("\nPresione enter para continuar.")
                                                clear_flag()
                                                break

                                elif selected_submenu3 == "r":
                                    clear_flag()
                            else:
                                invalid_selection()                                    

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
