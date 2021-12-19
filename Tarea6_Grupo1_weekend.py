__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez, Marco Cordoba'

# ----------------------
# Importación de Módulos
# ----------------------

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

while selected_menu != "s":
    print(f"{TextFormat.GREEN}\n--------------------- PROGRAMACIÓN Y ESPECIALIZACIÓN EN PYTHON ---------------------\n"
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
                        print(f"\n{TextFormat.CYAN}Creación de Nuevo Programa\n{TextFormat.CLEAR}")
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

                                for i in Program.instances:
                                    if program_name == i.program_name:
                                        raise ValueError(f"\nYa existe un programa con el nombre \"{program_name}\".")

                            except ValueError as arg:
                                print(arg)
                                continue
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
                                continue
                            else:
                                break

                        locals()[program_name].principal = principal_name   

                        while True:
                            try:
                                locals()[program_name].max_students = int(input("\nMáxima cantidad de alumnos: "))
                                if locals()[program_name].max_students == False:
                                    raise SyntaxError
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros.")
                                continue
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                locals()[program_name].min_students = int(input("\nMínima cantidad de alumnos: "))
                                if locals()[program_name].min_students == False:
                                    raise SyntaxError
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros.")
                                continue
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                locals()[program_name].max_courses = int(input("\nMáxima cantidad de cursos: "))
                                if locals()[program_name].max_courses == False:
                                    raise SyntaxError
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros.")
                                continue
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                locals()[program_name].min_courses = int(input("\nMínima cantidad de cursos: "))
                                if locals()[program_name].min_courses == False:
                                    raise SyntaxError
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros.")
                                continue
                            except SyntaxError:
                                continue
                            else:
                                break

                        while True:
                            try:
                                locals()[program_name].program_duration = int(input("\nDuración del programa en años: "))  
                                if locals()[program_name].program_duration == False:
                                    raise SyntaxError
                            except ValueError:
                                print("\nDebe ingresar únicamente números enteros.")
                                continue
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
                                print(f"\nEl programa {locals()[program_name].program_name} no se creara.")
                                del locals()[program_name]                                
                                input("\nPulse enter para continuar.")
                                clear_flag()
                                break
                    #clear_flag()
                # if selected_submenu1 == "c":
                #     pass
                #     clear_flag()
                # if selected_submenu1 == "m":
                #     pass
                #     clear_flag()
                # if selected_submenu1 == "e":
                #     pass
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
