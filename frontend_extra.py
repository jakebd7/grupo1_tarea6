import copy
from time import sleep
from typing import Coroutine
from classroom import Classroom
from person import Person
from tuition import Tuition
from course import Course
from program import Program
from teacher_type import Teacher_type
from turn import Turn
from building import Building
from analitycs import Analitycs

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


def name_check_with_numbers(clase: str, new = False):
    select = int
    del_dela = "del"
    if clase == "programa":
        select = 1
    elif clase == "curso":
        select = 2
    elif clase == "turno":
        select = 3
    elif clase == "aula":
        select = 4
    elif clase == "edificio":
        select = 5
    elif clase == "tipo de profesor":
        select = 6
    elif clase == "matricula":
        select = 7 
        del_dela = "de la"
    else:
        print("\nNo ingreso una clase válida.")
        return

    var1 = str
    var2 = str
    if new == True:
        var1 = "Nuevo n"
        var2 = " nuevo "
    else:
        var1 = "N"
        var2 = " "

    instance_name = str
    while True:
        try:
            instance_name = input(f"\n{var1}ombre {del_dela} {clase}: ") 
            only_white_spaces = True
            for i in instance_name:
                if i != " ":
                    only_white_spaces = False
                    break
                                
            only_underscores = True
            for i in instance_name:
                if i != "_":
                    only_underscores = False
                    break
                                    
            if only_white_spaces == True:
                raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} no debe contener únicamente espacios vacíos.")
            elif only_underscores == True:
                raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} no debe contener únicamente guiones bajos.") 

            for i in instance_name:
                if i.isalnum() == False:
                    if i != " " and i != "_":
                        raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} solo puede contener letras, números, espacios vacíos y guiones bajos.")                             

            if select == 1:
                for instance in Program.instances:
                    if instance_name == instance.program_name: 
                        raise ValueError(f"\nYa existe un programa con el nombre \"{instance_name}\".")
            
            elif select == 2:
                for instance in Course.instances:
                    if instance_name == instance.course_name: 
                        raise ValueError(f"\nYa existe un curso con el nombre \"{instance_name}\".")

            elif select == 3:
                for instance in Turn.instances:
                    if instance_name == instance.turn: 
                        raise ValueError(f"\nYa existe un turno con el nombre \"{instance_name}\".")

            elif select == 4:
                for instance in Classroom.instances:
                    if instance_name == instance.classroom_name: 
                        raise ValueError(f"\nYa existe un aula con el nombre \"{instance_name}\".")

            elif select == 5:
                for instance in Building.instances:
                    if instance_name == instance.name: 
                        raise ValueError(f"\nYa existe un edificio con el nombre \"{instance_name}\".")

            elif select == 6:
                for instance in Teacher_type.instances:
                    if instance_name == instance.type_teacher: 
                        raise ValueError(f"\nYa existe un tipo de profesor con el nombre \"{instance_name}\".")
            
            elif select == 7:
                for instance in Tuition.instances:
                    if instance_name == instance.name: 
                        raise ValueError(f"\nYa existe una matricula con el nombre \"{instance_name}\".")

        except ValueError as arg:
            print(arg)
        except KeyError:
            break
        else:
            break  

    return instance_name

def name_check_no_numbers(class_instance, new = False, attribute = None):
    select = int
    class_name = str
    del_dela = "del"
    if type(class_instance) is Program:
        select = 1
        class_name = "director"
    elif type(class_instance) is Course:
        select = 2
        class_name = "curso"
    elif type(class_instance) is Person:
        select = 3
        if class_instance in Person.instances_student:
            class_name = "estudiante"
        elif class_instance in Person.instances_teacher:
            class_name = "profesor"
    elif type(class_instance) is Classroom:
        select = 4
        class_name = "aula"
    elif type(class_instance) is Building:
        select = 5
        class_name = "edificio"
    elif type(class_instance) is Teacher_type:
        select = 6
        class_name = "tipo de profesor"
    elif type(class_instance) is Turn:
        select = 7
        class_name = "turno"
    elif type(class_instance) is Tuition:
        select = 8
        class_name = "matricula"
        del_dela = "de la"
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return 

    var1 = str
    var2 = str
    var3 = str
    if new == True:
        if select == 3 and attribute == "last_name":
            var1 = "Nuevo apellido"
            var2 = " nuevo "
            var3 = "apellido"
        else:
            var1 = "Nuevo nombre"
            var2 = " nuevo "
            var3 = "nombre"

    else:
        if select == 3 and attribute == "last_name":        
            var1 = "Apellido" 
            var2 = " "
            var3 = "apellido"
        else:
            var1 = "Nombre" 
            var2 = " "
            var3 = "nombre"

    name = str
    while True:
        try:
            name = input(f"\n{var1} {del_dela} {class_name}: ")

            only_white_spaces = True
            for i in name:
                if i != " ":
                    only_white_spaces = False
                    break
                                
            only_underscores = True
            for i in name:
                if i != "_":
                    only_underscores = False
                    break
                                    
            if only_white_spaces == True:
                raise ValueError(f"\nEl{var2}{var3} {del_dela} {class_name} no debe contener únicamente espacios vacíos.")
            elif only_underscores == True:
                raise ValueError(f"\nEl{var2}{var3} {del_dela} {class_name} no debe contener únicamente guiones bajos.")

            for i in name:
               if i.isalpha() == False:
                    if i != " " and i != "_":  
                        raise ValueError(f"\nEl{var2}{var3} {del_dela} {class_name} solo puede contener letras, espacios vacíos y guiones bajos.")                               

        except ValueError as arg:
            print(arg)
        else:
            break  

    if new == True:    
        while True:
            change_check = input(f"\nConfirme que desea cambiar el {var3} {del_dela} {class_name} de \"{getattr(class_instance, attribute)}\" a \"{name}\" (S/N): ").lower() 

            if change_check == "s": 
                setattr(class_instance, attribute, name)                                                    
                print(f"\nEl nuevo {var3} {del_dela} {class_name} {del_dela} es \"{getattr(class_instance, attribute)}\".")
                break
            
            elif change_check == "n":
                print(f"\nNo se realizo ningún cambio, el {var3} {del_dela} {class_name} continua siendo \"{getattr(class_instance, attribute)}\".")
                break
    else:
        setattr(class_instance, attribute, name)  

def name_check_non_existence(clase: str, new = False):
    select = int
    del_dela = "del"
    un_una = "un"
    if clase == "programa":
        select = 1
    elif clase == "curso":
        select = 2
    elif clase == "turno":
        select = 3
    elif clase == "aula":
        select = 4
    elif clase == "edificio":
        select = 5
    elif clase == "tipo de profesor":
        select = 6
    elif clase == "matricula":
        select = 7
        del_dela = "de la"
        un_una = "una"
    elif clase == "estudiante":
         select = 8
    elif clase == "profesor":
         select = 9
    else:
        print("\nNo ingreso una clase válida.")
        return

    var1 = str
    var2 = str
    if new == True:
        var1 = "Nuevo n"
        var2 = " nuevo "
    else:
        var1 = "N"
        var2 = " "

    instance_name = str
    while True:
        try:
            instance_name = input(f"\n{var1}ombre {del_dela} {clase}: ")  
            only_white_spaces = True
            for i in instance_name:
                if i != " ":
                    only_white_spaces = False
                    break
                                
            only_underscores = True
            for i in instance_name:
                if i != "_":
                    only_underscores = False
                    break
                                    
            if only_white_spaces == True:
                raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} no debe contener únicamente espacios vacíos.") 
            elif only_underscores == True:
                raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} no debe contener únicamente guiones bajos.")

            for i in instance_name:
                if i.isalnum() == False:
                    if i != " " and i != "_":
                        raise ValueError(f"\nEl{var2}nombre {del_dela} {clase} solo puede contener letras, números, espacios vacíos y guiones bajos.")                              

            instance_check = False
            if select == 1:
                for instance in Program.instances:
                    if instance_name == instance.program_name: 
                        instance_check = True
            
            elif select == 2:
                for instance in Course.instances:
                    if instance_name == instance.course_name: 
                        instance_check = True

            elif select == 3:
                for instance in Turn.instances:
                    if instance_name == instance.turn: 
                        instance_check = True

            elif select == 4:
                for instance in Classroom.instances:
                    if instance_name == instance.classroom_name: 
                        instance_check = True

            elif select == 5:
                for instance in Building.instances:
                    if instance_name == instance.name: 
                        instance_check = True

            elif select == 6:
                for instance in Teacher_type.instances:
                    if instance_name == instance.type_teacher: 
                        instance_check = True
            
            elif select == 7:
                for instance in Tuition.instances:
                    if instance_name == instance.name: 
                        instance_check = True

            elif select == 8:
                for instance in Person.instances_student:
                    if instance_name == instance.name: 
                        instance_check = True

            elif select == 9:
                for instance in Person.instances_teacher:
                    if instance_name == instance.name: 
                        instance_check = True

            if instance_check == False:
                raise SyntaxError(f"\nNo existe {un_una} {clase} con el nombre \"{instance_name}\".")

        except ValueError as arg:
            print(arg)
        except SyntaxError as arg:
            print(arg)
        else:
            break  

    return instance_name

def id_check(clase: str):
    if clase == "estudiante":
        select = 1
    elif clase == "profesor":
        select = 2   
    else:
        print("\nNo ingreso una clase válida.")
        return
        
    teacher_student = int
    while True:
        try:
            id = int(input(f"\nId del {clase}: "))
            if id < 0:
                raise SyntaxError(f"\nLos id de los {clase} no son números negativos.")

            check = False
            if select == 1:
                for instance in Person.instances_student:
                    if id == instance.id_student: 
                        teacher_student = instance.name                                        
                        check = True
            elif select == 2:
                for instance in Person.instances_teacher:
                    if id == instance.id_teacher:
                        teacher_student = instance.name
                        check = True

            if check == False:      
                raise SyntaxError(f"\nNo existe ningún {clase} con el id: \"{id}\".")

        except ValueError:
            print("\nDebe ingresar únicamente números enteros.")
        except SyntaxError as arg:
            print(arg)
        except KeyError:
            break
        else:
            break

    return teacher_student

def set_change_attr_number(class_instance, new = False, attribute = None):
    if not (hasattr(class_instance, attribute)):
        print(f"\nEl atributo \"{attribute}\" no existe en la clase \"{class_instance}\".")
        return

    select = int
    attr = str
    class_name = str
    class_txt = str
    if type(class_instance) is Program:
        select = 1
        class_name = "programa"
    elif type(class_instance) is Course:
        select = 2
        class_name = "curso"
        if attribute == "credits":
            input_txt = "reditos"
            check_txt1 = "los creditos"
            check_txt2 = "Los nuevo creditos"
            check_txt3 = "son"
        elif attribute == "week_hours":
            input_txt = "oras semanales"
            check_txt1 = "la cantidad de horas semanales"
            check_txt2 = "La nueva cantidad de horas semanales"
            check_txt3 = "son"
        elif attribute == "price":
            input_txt = "recio"
            check_txt1 = "el precio"
            check_txt2 = "El nuevo precio"
            check_txt3 = "es"
        elif attribute == "id_profesor":
            input_txt = "ipo de profesor"
            check_txt1 = "el tipo de profesor"
            check_txt2 = "El nuevo tipo de profesor"
            check_txt3 = "es"
    elif type(class_instance) is Person:
        select = 3
        if class_instance in Person.instances_student:
            class_name = "estudiante"
        elif class_instance in Person.instances_teacher:
            class_name = "profesor"
    elif type(class_instance) is Classroom:
        select = 4
        class_name = "aula"
    elif type(class_instance) is Building:
        select = 5
        class_name = "edificio"
    elif type(class_instance) is Teacher_type:
        select = 6
        class_name = "tipo de profesor"
    elif type(class_instance) is Turn:
        select = 7
        class_name = "turno"
    elif type(class_instance) is Tuition:
        select = 8
        class_name = "matricula"
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    var = str
    if new == True:
        if select == 2:
            if attribute == "credits":
                var = "Nuevos c"
            elif attribute == "week_hours":
                var = "Nuevas h"
            elif attribute == "price":
                var = "Nuevo p"
            elif attribute == "id_profesor":
                var = "Nuevo t"
    else:
        if select == 2:
            if attribute == "credits":        
                var = "C"
            elif attribute == "week_hours":
                var = "H"
            elif attribute == "price":
                var = "P"
            elif attribute == "id_profesor":
                var = "T"    

    number = int
    while True:
        try:
            number = int(input(f"\n{var}{input_txt} del {class_name}: "))
            if number < 0:
                setattr(class_instance, attribute, number)
                raise SyntaxError    
        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break    

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar {check_txt1} del {class_name} de \"{getattr(class_instance, attribute)}\" a \"{number}\" (S/N): ").lower()
            if change_check == "s":
                setattr(class_instance, attribute, number)                                               
                print(f"\n{check_txt2} del {class_name} {check_txt3} \"{getattr(class_instance, attribute)}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo ningún cambio, {check_txt1} del {class_name} continua siendo \"{getattr(class_instance, attribute)}\".")
                break
    else:
        setattr(class_instance, attribute, number)          

def max_students_check(class_instance, new = False):
    class_name = str
    student_seats = str   
    select = int
    if type(class_instance) is Program:
        class_name = "programa"
        student_seats = "estudiantes"
        select = 1
    elif type(class_instance) is Course:
        class_name = "curso"
        student_seats = "estudiantes"
        select = 1
    elif type(class_instance) is Classroom:
        class_name = "aula"
        student_seats = "asientos"
        select = 2
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.")
        return

    var = str
    if new == True:
        var = "Nueva c"
    else:
        var = "C"

    while True:
        try:
            max_students = int(input(f"\n{var}antida máxima de {student_seats}: "))
            if select == 1:
                if max_students <= 0 or max_students < class_instance.min_students:
                    class_instance.max_students = max_students
                    raise SyntaxError    
            else:
                if max_students < 0:
                    class_instance.seats_capacity = max_students
                    raise SyntaxError 
        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar la cantidad máxima de {student_seats} del {class_name} de \"{class_instance.max_students}\" a \"{max_students}\" (S/N): ").lower()
            if change_check == "s":
                if select == 1:
                    class_instance.max_students = max_students 
                else:
                    class_instance.seats_capacity = max_students

                print(f"\nLa nueva cantidad máxima de {student_seats} del {class_name} es \"{class_instance.max_students}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo níngun cambio, la cantidad máxima de {student_seats} del {class_name} continua siendo \"{class_instance.max_students}\".")
                break
    else:
        if select == 1:
            class_instance.max_students = max_students
        else:
            class_instance.seats_capacity = max_students        

def min_students_check(class_instance, new = False):
    class_name = str
    student_seats = str   
    select = int
    if type(class_instance) is Program:
        class_name = "programa"
    elif type(class_instance) is Course:
        class_name = "curso"
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.")
        return

    var = str

    if new == True:
        var = "Nueva c"
    else:
        var = "C"

    while True:
        try:
            min_students = int(input(f"\n{var}antida mínima de estudiantes: "))
            if min_students < 0 or min_students > class_instance.max_students:
                class_instance.min_students = min_students
                raise SyntaxError    

        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar la cantidad mínima de alumnos del {class_name} de \"{class_instance.min_students}\" a \"{min_students}\" (S/N): ").lower()
            if change_check == "s":
                class_instance.min_students = min_students                                                        
                print(f"\nLa nueva cantidad mínima de alumnos del {class_name} es \"{class_instance.min_students}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo ningún cambio, la cantidad mínima de alumnos del {class_name} continua siendo \"{class_instance.min_students}\".")
                break
    else:
        class_instance.min_students = min_students    

def max_courses_check(class_instance, new = False):
    if type(class_instance) is Program:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.")    
        return

    var = str
    if new == True:
        var = "Nueva c"
    else:
        var = "C"

    max_courses = int
    while True:
        try:
            max_courses = int(input(f"\n{var}antida máxima de cursos: "))
            if max_courses <= 0 or max_courses < class_instance.min_courses:
                class_instance.max_courses = max_courses
                raise SyntaxError    
        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar la cantidad máxima de cursos del programa de \"{class_instance.max_courses}\" a \"{max_courses}\" (S/N): ").lower()
            if change_check == "s":
                class_instance.max_courses = max_courses                                                      
                print(f"\nLa nueva cantidad máxima de cursos del programa es \"{class_instance.max_courses}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo ningún cambio, la cantidad máxima de cursos del programa continua siendo \"{class_instance.max_courses}\".")
                break
    else:
        class_instance.max_courses = max_courses

def min_courses_check(class_instance, new = False):
    if type(class_instance) is Program:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return

    var = str
    if new == True:
        var = "Nueva c"
    else:
        var = "C"

    while True:
        try:
            min_courses = int(input(f"\n{var}antida mínima de cursos: "))
            if min_courses < 0 or min_courses > class_instance.max_courses:
                class_instance.min_courses = min_courses
                raise SyntaxError    
        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break  

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar la cantidad mínima de cursos del programa de \"{class_instance.min_courses}\" a \"{min_courses}\" (S/N): ").lower()
            if change_check == "s":
                class_instance.min_courses = min_courses                                                     
                print(f"\nLa nueva cantidad mínima de cursos del programa es \"{class_instance.min_courses}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo ningún cambio, la cantidad mínima de cursos del programa continua siendo \"{class_instance.min_courses}\".")
                break
    else:
        class_instance.min_courses = min_courses

def program_duration_check(class_instance, new = False):
    if type(class_instance) is Program:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return   

    var = str
    if new == True:
        var = "Nueva d"
    else:
        var = "D"
    
    program_duration = int
    while True:
        try:
            program_duration = int(input(f"\n{var}uración del programa en años: "))  
            if program_duration != 4 and program_duration != 5:
                class_instance.program_duration = program_duration
                raise SyntaxError    
        except ValueError:
            print("\nDebe ingresar únicamente números enteros positivos.")
        except SyntaxError:
            continue
        else:
            break  

    if new == True:
        while True:
            change_check = input(f"\nConfirme que desea cambiar la duración (en años) del programa de \"{class_instance.program_duration}\" a \"{program_duration}\" (S/N): ").lower()
            if change_check == "s":
                class_instance.program_duration = program_duration                                                   
                print(f"\nLa nueva duración (en años) del programa es \"{class_instance.program_duration}\".")
                break
            elif change_check == "n":
                print(f"\nNo se realizo níngun cambio, la duración (en años) del programa continua siendo \"{class_instance.program_duration}\".")
                break
    else:
        class_instance.program_duration = program_duration

def program_information_show(class_instance):
    if type(class_instance) is Program:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    print(f"\nEl programa \"{class_instance.program_name}\" tiene la siguiente información asociada: \n"
          f"\nNombre del Programa: {class_instance.program_name}\n"
          f"Fecha de Creación del Programa: {class_instance.creation_date_program}\n"
          f"Estatus del Programa: {class_instance.program_status}\n"
          f"Director: {class_instance.principal}\n"
          f"Número de Cursos del Programa: {len(class_instance.courses)}\n"
          f"Máximo de Estudiantes: {class_instance.max_students}\n"
          f"Mínimo de Estudiantes: {class_instance.min_students}\n"
          f"Máximo de Cursos: {class_instance.max_courses}\n"
          f"Mínimo de Cursos: {class_instance.min_courses}\n"                            
          f"Duración del Programa en años: {class_instance.program_duration}")    

def course_information_show(class_instance):
    if type(class_instance) is Course:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return 

    print(f"\nLa información asociada al curso \"{class_instance.course_name}\" es: "
           "\n"
          f"\nNombre del Curso: {class_instance.course_name}\n"
          f"Creditos del Curso: {class_instance.credits}\n"
          f"Cantidad de Horas Semanales: {class_instance.week_hours}")
          
    if class_instance.program == "No Establecido":
        print(f"Programa en el que esta el Curso: No Establecido")
    else:
        print(f"Programa en el que esta el Curso: {class_instance.program.program_name}")
          
    print(f"Precio del Curso: {class_instance.price}")

    if class_instance.teacher == "No Establecido":
        print(f"Profesor del Curso: No Establecido")
    else:
        print(f"Profesor del Curso: {class_instance.teacher.name} {class_instance.teacher.last_name}\n"
              f"Id Profesor del Curso: {class_instance.teacher.id_teacher}")
          
    print(f"Estatus del Curso: {class_instance.course_status}\n"
          f"Máximo de Estudiantes: {class_instance.max_students}\n"
          f"Mínimo de Estudiantes: {class_instance.min_students}")

def set_attribute_in_list_in_instance(class_instance, attribute_list = None, attritube = None, input_x = None):
    if isinstance(class_instance, Program):
        pass
    elif isinstance(class_instance, Course):
        pass
    elif isinstance(class_instance, Person):
        pass
    elif isinstance(class_instance, Classroom):
        pass
    elif isinstance(class_instance, Building):
        pass
    elif isinstance(class_instance, Teacher_type):
        pass
    elif isinstance(class_instance, Turn):
        pass
    elif isinstance(class_instance, Tuition):
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    for instance in getattr(class_instance, attribute_list):
        setattr(instance, attritube, input_x)

def del_instance_in_other_instance_list(class_instance, attribute_0 = None, attritube_1 = None):
    if isinstance(class_instance, Program):
        pass
    elif isinstance(class_instance, Course):
        pass
    elif isinstance(class_instance, Person):
        if class_instance in Person.instances_student:
            pass
        elif class_instance in Person.instances_teacher:
            pass
    elif isinstance(class_instance, Classroom):
        pass
    elif isinstance(class_instance, Building):
        pass
    elif isinstance(class_instance, Teacher_type):
        pass
    elif isinstance(class_instance, Turn):
        pass
    elif isinstance(class_instance, Tuition):
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    for instance in getattr(getattr(class_instance, attribute_0), attritube_1):
        if class_instance == instance: 
            instance_index = getattr(getattr(class_instance, attribute_0), attritube_1).index(instance)
            del getattr(getattr(class_instance, attribute_0), attritube_1)[instance_index]

def del_instance_in_class(class_instance):
    attribute_class_instance = "instances"
    if isinstance(class_instance, Program):
        pass
    elif isinstance(class_instance, Course):
        pass
    elif isinstance(class_instance, Person):
        if class_instance in Person.instances_student:
            attribute_class_instance = "instances_student"
        elif class_instance in Person.instances_teacher:
            attribute_class_instance = "instances_teacher"
    elif isinstance(class_instance, Classroom):
        pass
    elif isinstance(class_instance, Building):
        pass
    elif isinstance(class_instance, Teacher_type):
        pass
    elif isinstance(class_instance, Turn):
        pass
    elif isinstance(class_instance, Tuition):
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    for instance in getattr(class_instance, attribute_class_instance): 
        if class_instance == instance:
            instance_index = getattr(class_instance, attribute_class_instance).index(instance)
            del getattr(class_instance, attribute_class_instance)[instance_index]

def change_instance_name(class_instance, new_name):
    attribute = str
    class_name = str
    del_dela = "del"
    if type(class_instance) is Program:
        attribute = "program_name"
        class_name = "programa"
    elif type(class_instance) is Course:
        attribute = "course_name"
        class_name = "curso"
    elif type(class_instance) is Person:
        attribute = "name"
        if class_instance in Person.instances_student:
            class_name = "estudiante"
        elif class_instance in Person.instances_teacher:
            class_name = "profesor"
    elif type(class_instance) is Classroom:
        attribute = "classroom_name"
        class_name = "aula"
    elif type(class_instance) is Building:
        attribute = "name"
        class_name = "edificio"
    elif type(class_instance) is Teacher_type:
        attribute = "type_teacher"
        class_name = "tipo de profesor"
    elif type(class_instance) is Turn:
        attribute = "turn"
        class_name = "turno"
    elif type(class_instance) is Tuition:
        attribute = "name"
        class_name = "matricula"
        del_dela = "de la"
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return 

    var = []

    while True:
        change_check = input(f"\nConfirme que desea cambiar el nombre {del_dela} {class_name} de \"{getattr(class_instance, attribute)}\" a \"{new_name}\" (S/N): ").lower()

        if change_check == "s":
            locals()[new_name] = copy.deepcopy(class_instance)

            setattr(locals()[new_name], attribute, new_name)

            if class_instance in Person.instances_student:

                for instance in Person.instances_student:
                    if class_instance == instance:
                        instance_index = Person.instances_student.index(instance)
                        del Person.instances_student[instance_index]
                                                    
                Person.instances_student.append(locals()[new_name])                
            
            elif class_instance in Person.instances_teacher:

                for instance in Person.instances_teacher:
                    if class_instance == instance:
                        instance_index = Person.instances_teacher.index(instance)
                        del Person.instances_teacher[instance_index]
                                                    
                Person.instances_teacher.append(locals()[new_name])  

            else:

                for instance in class_instance.__class__.instances:
                    if class_instance == instance:
                        instance_index = class_instance.__class__.instances.index(instance)
                        del class_instance.__class__.instances[instance_index]
                                                    
                class_instance.__class__.instances.append(locals()[new_name])

            print(f"\nEl nuevo nombre {del_dela} {class_name} es \"{getattr(locals()[new_name], attribute)}\".")

            var = [True, locals()[new_name]]
            break
        elif change_check == "n":

            print(f"\nNo se realizo ningún cambio, el nombre {del_dela} {class_name} continua siendo \"{getattr(class_instance, attribute)}\".")
            var = [False]
            break    

    return var

def view_each_instance(class_instance, input1 = None, input2 = None, mode = None):
    class_name = str
    attribute = str
    attribute2 = str
    instance = str
    as_os = "os"
    no_include = str
    if isinstance(class_instance, Program):
        class_name = "programa"
        attribute = "program_name"
    elif isinstance(class_instance, Course):
        class_name = "curso"
        attribute = "course_name"
    elif isinstance(class_instance, Person): 
        attribute = "name"
        if class_instance in Person.instances_student:
            class_name = "estudiante"
            instance = "instances_student"
            attribute2 = "id_student"
        elif class_instance in Person.instances_teacher:
            class_name = "profesore"
            instance = "instances_teacher"
            attribute2 = "id_teacher"
    elif isinstance(class_instance, Classroom):
        class_name = "aula"
        attribute = "classroom_name"
        as_os = "as"
    elif isinstance(class_instance, Building):
        class_name = "edificio"
        attribute = "name"
    elif isinstance(class_instance, Teacher_type):
        class_name = "tipo de profesore"
        attribute = "type_teacher"
    elif isinstance(class_instance, Turn):
        class_name = "turno"
        attribute = "turn"
    elif isinstance(class_instance, Turn):
        class_name = "matricula"
        attribute = "name"
        as_os = "as"
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    inside_instance = str
    if mode == 3:
        if input1 == "courses":
            inside_instance = "curso"


    while True:
        if mode == 3:
            program_list = input(f"\nDesea ver una lista de tod{as_os} l{as_os} {inside_instance}s del {class_name} (S/N): ").lower()
        else:
            program_list = input(f"\nDesea ver una lista de tod{as_os} l{as_os} {class_name}s disponibles (S/N): ").lower()

        if program_list == "s":
            print("")
            
            counter = 0
            if isinstance(class_instance, Person): 
                if input1 == None and input2 == None and mode == None:
                    for i in range(0, len(getattr(class_instance, instance)),1):
                        print(f"({i}) {getattr(class_instance, instance)[i].name} {getattr(class_instance, instance)[i].last_name} => Id: {getattr(getattr(class_instance, instance)[i], attribute2)}")
                    break    
                
                elif mode == 1:
                    for i in range(0, len(getattr(class_instance, instance)),1):
                        if len(getattr(getattr(class_instance, instance)[i], input1)) < getattr(getattr(class_instance, instance)[i], input2):
                            print(f"({counter}) {getattr(class_instance, instance)[i].name} {getattr(class_instance, instance)[i].last_name} => Id: {getattr(getattr(class_instance, instance)[i], attribute2)}")
                            counter += 1 
                    break 

                elif mode == 2:
                    for i in range(0, len(getattr(class_instance, instance)),1):
                        if input1 == getattr(getattr(class_instance, instance)[i], input2):
                            print(f"({counter}) {getattr(class_instance, instance)[i].name} {getattr(class_instance, instance)[i].last_name} => Id: {getattr(getattr(class_instance, instance)[i], attribute2)}")
                            counter += 1  
                    break  
                elif mode == 3:
                    print("\nLogica no desarrollada para la clase Persona.")
                    #for i in range(0, len(getattr(class_instance, input1)),1):
                        #print(f"({i}) {getattr(class_instance, instance)[i].name} {getattr(class_instance, instance)[i].last_name} => Id: {getattr(getattr(class_instance, instance)[i], attribute2)}")
                    break
            else:
                if input1 == None and input2 == None and mode == None:
                    for i in range(0, len(class_instance.__class__.instances),1):                    
                        print(f"({i}) {getattr(class_instance.__class__.instances[i], attribute)}")
                    
                    break
                elif mode == 1:
                    for i in range(0, len(class_instance.__class__.instances),1):   
                        if len(getattr(class_instance.__class__.instances[i], input1)) < getattr(class_instance.__class__.instances[i], input2):
                            print(f"({counter}) {getattr(class_instance.__class__.instances[i], attribute)}")
                            counter += 1                      

                    break    
                elif mode == 2:
                    for i in range(0, len(class_instance.__class__.instances),1): 
                        if input1 == getattr(class_instance.__class__.instances[i], input2):
                            print(f"({counter}) {getattr(class_instance.__class__.instances[i], attribute)}")
                            counter += 1
                    break

                elif mode == 3:
                    for i in range(0, len(getattr(class_instance, input1)),1):   
                        print(f"({i}) {getattr(getattr(class_instance, input1)[i], input2)}")                        
                    break
            break
        elif program_list == "n":
            break

def courses_availability():
    var = False
    for instance in Course.instances:
        if "No Establecido" == instance.program:
            var = True
            break

    return var

def programs_availability():
    var = False
    for instance in Program.instances:
        if len(instance.courses) <= instance.max_courses:
            var = True
            break

    return var

def teachers_availability():
    var = False
    for instance in Person.instances_teacher:
        if len(instance.courses) <= instance.max_courses:
            var = True
            break

    return var

def add_requirements_check(class_instance, clase: str, list_parameter: str, max_parameter: str):
    class_name = str
    instance = "instances"
    var1 = "El"
    class_instances = None
    if isinstance(class_instance, Program):
        class_name = "programa"
    elif isinstance(class_instance, Person):
        if class_instance in Person.instances_teacher:
            class_name = "profesor"
            instance = "instances_teacher"
        if class_instance in Person.instances_student:
            class_name = "estudiante"
            instance = "instances_student"
    elif isinstance(class_instance, Course):
        class_name = "curso"
    else:
        print("\nClase_1 no valida.")
        return

    atributo = str
    if clase == "programa":        
        class_instances = Program.instances
        atributo = "program_name"
    elif clase == "estudiante":
        class_instances = Person.instances_student
        atributo = "name"
    elif clase == "profesor":
        class_instances = Person.instances_teacher
        atributo = "name"
    elif clase == "curso":
        class_instances = Course.instances
        atributo = "course_name"
    else:
        print("\nClase_2 no valida.")
        return

    existing_instance = str
    while True:
        if clase == "profesor" or clase == "estudiante":
            existing_instance = id_check(clase)
        else:
            existing_instance = name_check_non_existence(clase)
        for i in class_instances:
            if existing_instance == getattr(i, atributo):
                existing_instance = i
                break
        
        if len(getattr(existing_instance, list_parameter)) < getattr(existing_instance, max_parameter):
            break

    curse_not_in_name= False
    for instance_x in getattr(class_instance.__class__, instance):
        if not (instance_x in getattr(existing_instance, list_parameter)):
            curse_not_in_name = True
            break

    if curse_not_in_name == False:
        print(f"\nTodos los {class_name}s existentes ya estan agregados al {clase} \"{getattr(existing_instance, atributo)}\".")
        return [False]

    elif len(getattr(existing_instance, list_parameter)) > getattr(existing_instance, max_parameter):
        print(f"\nNo se pueden agregar mas {class_name}s al {clase} \"{getattr(existing_instance, atributo)}\". {var1} {clase} \"{getattr(existing_instance, atributo)}\" ya ha alcanzado la cantidad máxima de {class_name}s establecida.")
        return [False]
    else:
        return [True, existing_instance] 