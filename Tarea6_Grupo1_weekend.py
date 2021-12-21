__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez, Marco Cordoba'

# ----------------------
# Importación de Módulos
# ----------------------

import copy
from classroom import Classroom
from person import Person
from tuition import Tuition
from course import Course
from program import Program
from teacher_type import Teacher_type
from turn import Turn
from building import Building
from analitycs import Analitycs
from os import name, system
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
                  f"[A] {TextFormat.BOLD_UNDERLINE}A{TextFormat.CLEAR}gregar\n"
                  f"[C] {TextFormat.BOLD_UNDERLINE}C{TextFormat.CLEAR}onsultar\n"
                  f"[M] {TextFormat.BOLD_UNDERLINE}M{TextFormat.CLEAR}odificar\n"
                  f"[E] {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}liminar\n"
                  f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
            selected_submenu2 = input("Digite una opción: ").lower()
            if selected_submenu2 in "acme" and selected_submenu2 != "":
                if selected_submenu2 == "a":
                    if selected_submenu1 == "p":
                        clear_screen()
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Programa{TextFormat.CLEAR}")
                        program_name = str
                        while True:
                            try:
                                program_name = input("\nNombre del programa: ")
                                only_white_spaces = True
                                for i in program_name:
                                    if i != " ":
                                        only_white_spaces = False
                                        break
                                
                                if only_white_spaces == True:
                                    raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")

                                for i in program_name:
                                    if i.isalnum() == False:
                                        if i != " ":                                        
                                            raise ValueError("\nEl nombre del programa solo puede contener letras, números y espacios vacíos.")

                                for instance in Program.instances:
                                    if locals()[program_name] == instance: 
                                        raise ValueError(f"\nYa existe un programa con el nombre \"{program_name}\".")

                            except ValueError as arg:
                                print(arg)
                            except KeyError:
                                break
                            else:
                                break         

                        locals()[program_name] = Program(program_name)

                        principal_name = str
                        while True:
                            principal_name = input("\nNombre del director: ")
                            try:
                                only_white_spaces = True
                                for i in principal_name:
                                    if i != " ":
                                        only_white_spaces = False
                                        break
                                
                                if only_white_spaces == True:
                                    raise ValueError("\nEl nombre del director no debe contener únicamente espacios vacíos.")
                                
                                for i in principal_name:
                                    if i.isalpha() == False:
                                        if i != " ":
                                            raise ValueError("\nEl nombre del director solo puede contener letras y espacios vacíos.")
                                 
                            except ValueError as arg:
                                print(arg)
                            else:
                                break

                        locals()[program_name].principal = principal_name   

                        while True:
                            try:
                                max_students = int(input("\nMáxima cantidad de alumnos: "))
                                if max_students <= 0:
                                    locals()[program_name].max_students = max_students
                                    raise SyntaxError    
                                else:
                                    locals()[program_name].max_students = max_students
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros positivos.")
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                min_students = int(input("\nMínima cantidad de alumnos: "))
                                if min_students < 0:
                                    locals()[program_name].min_students = min_students
                                    raise SyntaxError    
                                else:
                                    locals()[program_name].min_students = min_students
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros positivos.")
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                max_courses = int(input("\nMáxima cantidad de cursos: "))
                                if max_courses <= 0:
                                    locals()[program_name].max_courses = max_courses
                                    raise SyntaxError    
                                else:
                                    locals()[program_name].max_courses = max_courses
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros positivos.")
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                min_courses = int(input("\nMínima cantidad de cursos: "))
                                if min_courses < 0:
                                    locals()[program_name].min_courses = min_courses
                                    raise SyntaxError    
                                else:
                                    locals()[program_name].min_courses = min_courses
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros positivos.")
                            except SyntaxError:
                                continue
                            else:
                                break


                        while True:
                            try:
                                program_duration = int(input("\nDuración del programa en años: "))  
                                if program_duration != 4 and program_duration != 5:
                                    locals()[program_name].program_duration = program_duration
                                    raise SyntaxError    
                                else:
                                    locals()[program_name].program_duration = program_duration
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros positivos.")
                            except SyntaxError:
                                continue
                            else:
                                break                       
                        
                        while True:
                            verification = input(f"\nDesea crear el programa \"{locals()[program_name].program_name}\" con la información asociada que ha ingresado (S/N): ").lower()
                            if verification == "s":
                                print(f"\n{TextFormat.CYAN}Se ha creado el programa \"{locals()[program_name].program_name}\" con la siguiente información asociada:\n{TextFormat.CLEAR}"
                                      f"\nNombre del Programa: {locals()[program_name].program_name}\n"
                                      f"Director: {locals()[program_name].principal}\n"
                                      f"Máximo de Estudiantes: {locals()[program_name].max_students}\n"
                                      f"Mínimo de Estudiantes: {locals()[program_name].min_students}\n"
                                      f"Máximo de Cursos: {locals()[program_name].max_courses}\n"
                                      f"Mínimo de Cursos: {locals()[program_name].min_courses}\n"                            
                                      f"Duración del Programa en años: {locals()[program_name].program_duration}\n")
                                        
                                input("Pulse enter para continuar.")
                                clear_flag()
                                break
                            elif verification == "n":
                                print(f"\n{TextFormat.CYAN}El programa \"{locals()[program_name].program_name}\" no se creara.{TextFormat.CLEAR}")
                                for instance in Program.instances:
                                    if locals()[program_name] == instance:
                                        instance_index = Program.instances.index(instance)
                                        del Program.instances[instance_index]
                                del locals()[program_name]
                                                                
                                input("\nPulse enter para continuar.")
                                clear_flag()
                                break
 
                if selected_submenu2 == "c":
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
                                
                            program_name = str
                            while True:
                                try:
                                    program_name = input("\nIngrese nombre del programa a consultar: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break
                                            
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " ":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números y espacios vacíos.")

                                    for instance in Program.instances:
                                        if locals()[program_name] == instance:
                                            pass

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\".")
                                else:
                                    break   
                                        
                            print(f"\nLa información asociada al programa \"{locals()[program_name].program_name}\" es: "
                                  "\n"
                                  f"\nNombre del Programa: {locals()[program_name].program_name}\n"
                                  f"Director: {locals()[program_name].principal}\n"
                                  f"Máximo de Estudiantes: {locals()[program_name].max_students}\n"
                                  f"Mínimo de Estudiantes: {locals()[program_name].min_students}\n"
                                  f"Máximo de Cursos: {locals()[program_name].max_courses}\n"
                                  f"Mínimo de Cursos: {locals()[program_name].min_courses}\n"                            
                                  f"Duración del Programa en años: {locals()[program_name].program_duration}")

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
                            program_name = str
                            while True:
                                try:
                                    program_name = input("\nIngrese nombre del programa a modificar: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break
                                    
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " ":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números y espacios vacíos.")

                                    for instance in Program.instances:
                                        if locals()[program_name] == instance:
                                            pass

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\".")
                                else:
                                    break         

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
                                    new_program_name = str
                                    while True:
                                        try:
                                            new_program_name = input("\nIngrese nuevo nombre del programa: ")
                                            only_white_spaces = True
                                            for i in new_program_name:
                                                if i != " ":
                                                    only_white_spaces = False
                                                    break
                                    
                                            if only_white_spaces == True:
                                                raise ValueError("\nEl nuevo nombre del programa no debe contener únicamente espacios vacíos.")

                                            for i in new_program_name:
                                                if i.isalnum() == False:
                                                    if i != " ":                                        
                                                        raise ValueError("\nEl nuevo nombre del programa solo puede contener letras, números y espacios vacíos.")

                                            for instance in Program.instances:
                                                if locals()[new_program_name] == instance:
                                                    raise ValueError(f"\nYa existe un programa con el nombre \"{new_program_name}\".")

                                        except ValueError as arg:
                                            print(arg)
                                        except KeyError:
                                            break
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar el nombre del programa de \"{locals()[program_name].program_name}\" a \"{new_program_name}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[new_program_name] = copy.deepcopy(locals()[program_name])
                                            locals()[new_program_name].program_name = new_program_name
                                            for instance in Program.instances:
                                                if locals()[program_name] == instance:
                                                    instance_index = Program.instances.index(instance)
                                                    del Program.instances[instance_index]
                                            
                                            del locals()[program_name]               
                                            Program.instances.append(locals()[new_program_name])
                                            print(f"\nEl nuevo nombre del programa es \"{locals()[new_program_name].program_name}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, el nombre del programa continua siendo \"{locals()[program_name].program_name}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "d": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Nombre del Director del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")
                                    new_principal = str
                                    while True:
                                        try:
                                            new_principal = input("\nIngrese nuevo nombre del director del programa: ")
                                            only_white_spaces = True
                                            for i in new_principal:
                                                if i != " ":
                                                    only_white_spaces = False
                                                    break
                                    
                                            if only_white_spaces == True:
                                                raise ValueError("\nEl nuevo nombre del director del programa no debe contener únicamente espacios vacíos.")

                                            for i in new_principal:
                                                if i.isalnum() == False:
                                                    if i != " ":                                        
                                                        raise ValueError("\nEl nuevo nombre del director del programa solo puede contener letras, números y espacios vacíos.")

                                        except ValueError as arg:
                                            print(arg)
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar el nombre del director del programa de \"{locals()[program_name].principal}\" a \"{new_principal}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].principal = new_principal                                                          
                                            print(f"\nEl nuevo nombre del director del programa es \"{locals()[program_name].principal}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, el nombre del director del programa continua siendo \"{locals()[program_name].principal}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "e": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_max_students = int                               
                                    while True:
                                        try:
                                            new_max_students = int(input("\nIngrese la nueva cantidad máxima de alumnos que tendra el programa: "))
                                            if new_max_students <= 0 or new_max_students < locals()[program_name].min_students:
                                                locals()[program_name].max_students = new_max_students
                                                raise SyntaxError
                                        except ValueError:
                                            print("\nDebe ingresar únicamente números enteros positivos.")
                                        except SyntaxError:
                                            continue
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar la cantidad máxima de alumnos del programa de \"{locals()[program_name].max_students}\" a \"{new_max_students}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].max_students = new_max_students                                                        
                                            print(f"\nLa nueva cantidad máxima de alumnos del programa es \"{locals()[program_name].max_students}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, la cantidad máxima de alumnos del programa continua siendo \"{locals()[program_name].max_students}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "s": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Alumnos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_min_students = int                               
                                    while True:
                                        try:
                                            new_min_students = int(input("\nIngrese la nueva cantidad mínima de alumnos que tendra el programa: "))
                                            if new_min_students < 0 or new_min_students > locals()[program_name].max_students:
                                                locals()[program_name].min_students = new_min_students
                                                raise SyntaxError
                                        except ValueError:
                                            print("\nDebe ingresar únicamente números enteros positivos.")
                                        except SyntaxError:
                                            continue
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar la cantidad mínima de alumnos del programa de \"{locals()[program_name].min_students}\" a \"{new_min_students}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].min_students = new_min_students                                                        
                                            print(f"\nLa nueva cantidad mínima de alumnos del programa es \"{locals()[program_name].min_students}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, la cantidad mínima de alumnos del programa continua siendo \"{locals()[program_name].min_students}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "c": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Máxima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_max_courses = int                               
                                    while True:
                                        try:
                                            new_max_courses = int(input("\nIngrese la nueva cantidad máxima de cursos que tendra el programa: "))
                                            if new_max_courses <= 0 or new_max_courses < locals()[program_name].min_courses:
                                                locals()[program_name].max_courses = new_max_courses
                                                raise SyntaxError
                                        except ValueError:
                                            print("\nDebe ingresar únicamente números enteros positivos.")
                                        except SyntaxError:
                                            continue
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar la cantidad máxima de cursos del programa de \"{locals()[program_name].max_courses}\" a \"{new_max_courses}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].max_courses = new_max_courses                                                      
                                            print(f"\nLa nueva cantidad máxima de cursos del programa es \"{locals()[program_name].max_courses}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, la cantidad máxima de cursos del programa continua siendo \"{locals()[program_name].max_courses}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "u": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Cantidad Mínima de Cursos del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_min_courses = int                               
                                    while True:
                                        try:
                                            new_min_courses = int(input("\nIngrese la nueva cantidad mínima de cursos que tendra el programa: "))
                                            if new_min_courses < 0 or new_min_courses > locals()[program_name].max_courses:
                                                locals()[program_name].min_courses = new_min_courses
                                                raise SyntaxError
                                        except ValueError:
                                            print("\nDebe ingresar únicamente números enteros positivos.")
                                        except SyntaxError:
                                            continue
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar la cantidad mínima de cursos del programa de \"{locals()[program_name].min_courses}\" a \"{new_min_courses}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].min_courses = new_min_courses                                                     
                                            print(f"\nLa nueva cantidad mínima de cursos del programa es \"{locals()[program_name].min_courses}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, la cantidad mínima de cursos del programa continua siendo \"{locals()[program_name].min_courses}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                                elif selected_submenu3 == "g": 
                                    clear_screen()
                                    print(f"\n{TextFormat.CYAN}Sub Menú - Modificar Duración del Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")

                                    new_program_durations = int                               
                                    while True:
                                        try:
                                            new_program_durations = int(input("\nIngrese la nueva duración (en años) que tendra el programa: "))
                                            if new_program_durations != 4 and new_program_durations != 5:
                                                locals()[program_name].program_duration = new_program_durations
                                                raise SyntaxError
                                        except ValueError:
                                            print("\nDebe ingresar únicamente números enteros positivos.")
                                        except SyntaxError:
                                            continue
                                        else:
                                            break
                                    
                                    while True:
                                        change_check = input(f"\nConfirme que desea cambiar la duración (en años) del programa de \"{locals()[program_name].program_duration}\" a \"{new_program_durations}\" (S/N): ").lower()
                                        if change_check == "s":
                                            locals()[program_name].program_duration = new_program_durations                                                    
                                            print(f"\nLa nueva duración (en años) del programa es \"{locals()[program_name].program_duration}\".")
                                            break
                                        elif change_check == "n":
                                            print(f"\nNo se realizo níngun cambio, la duración (en años) del programa continua siendo \"{locals()[program_name].program_duration}\".")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                            elif selected_submenu3 == "r":
                                clear_flag()
                            else:
                                invalid_selection()
                #     clear_flag()
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
                                    program_name = input("\nIngrese nombre del programa a eliminar: ")
                                    only_white_spaces = True
                                    for i in program_name:
                                        if i != " ":
                                            only_white_spaces = False
                                            break
                                    
                                    if only_white_spaces == True:
                                        raise ValueError("\nEl nombre del programa no debe contener únicamente espacios vacíos.")

                                    for i in program_name:
                                        if i.isalnum() == False:
                                            if i != " ":                                        
                                                raise ValueError("\nEl nombre del programa solo puede contener letras, números y espacios vacíos.")

                                    for instance in Program.instances:
                                        if locals()[program_name] == instance:
                                            pass

                                except ValueError as arg:
                                    print(arg)
                                except KeyError:
                                    print(f"\nNo existe un programa con el nombre \"{program_name}\".")
                                else:
                                    break   

                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programa \"{locals()[program_name].program_name}\"\n{TextFormat.CLEAR}"
                                f"\n[E] {TextFormat.BOLD_UNDERLINE}E{TextFormat.CLEAR}liminar el programa \"{locals()[program_name].program_name}\"\n"
                                f"[R] {TextFormat.BOLD_UNDERLINE}R{TextFormat.CLEAR}egresar al Menú Principal\n")
                            selected_submenu3 = input("Digite una opción: ").lower() 
                            clear_screen()
                            print(f"\n{TextFormat.CYAN}Sub Menú - Eliminar Programa \"{locals()[program_name].program_name}\"{TextFormat.CLEAR}")
                            if selected_submenu3 in "er" and selected_submenu3 != "":     
                                if selected_submenu3 == "e":                                    
                                    while True:
                                        review_information = input(f"\nDesea revisar la información asociada al programa \"{locals()[program_name].program_name}\" antes de elimninarlo (S/N): ").lower()
                                        if review_information == "s":
                                            print(f"\nNombre del Programa: {locals()[program_name].program_name}\n"
                                                f"Director: {locals()[program_name].principal}\n"
                                                f"Máximo de Estudiantes: {locals()[program_name].max_students}\n"
                                                f"Mínimo de Estudiantes: {locals()[program_name].min_students}\n"
                                                f"Máximo de Cursos: {locals()[program_name].max_courses}\n"
                                                f"Mínimo de Cursos: {locals()[program_name].min_courses}\n"                            
                                                f"Duración del Programa en años: {locals()[program_name].program_duration}")
                                            break
                                        elif review_information == "n":
                                            break
                                        else:
                                            pass

                                    while True:
                                        print(f"\n{TextFormat.RED}La acción de eliminación no puede ser revertida, tenga cuidado con los programas que elimina.{TextFormat.CLEAR}")
                                        delete_check = input(f"\nConfirme eliminación del programa \"{locals()[program_name].program_name}\" (S/N): ").lower()
                                        if delete_check == "s":
                                            for instance in Program.instances:
                                                if locals()[program_name] == instance:
                                                    instance_index = Program.instances.index(instance)
                                                    del Program.instances[instance_index]
                                            
                                            del locals()[program_name]               
                                            print(f"\nEl programa de nombre \"{program_name}\" fue eliminado.")
                                            break
                                        elif delete_check == "n":
                                            print(f"\nNo se realizo níngun acción, el programa de nombre \"{locals()[program_name].program_name}\" no fue eliminado.")
                                            break
                                    
                                    input("\nPresione enter para continuar.")
                                    clear_flag()
                            elif selected_submenu3 == "r":
                                clear_flag()
                            else:
                                invalid_selection()                                    

                #     clear_flag()

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
