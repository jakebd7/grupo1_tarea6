import copy
from time import sleep
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
        var1 = "Nuevo a"
        var2 = "Nuevo n"
        var3 = " nuevo "

    else:
        var1 = "A"        
        var2 = "N"
        var3 = " "

    name = str
    while True:
        try:
            if select == 3 and attribute == "apellido":
                name = input(f"\n{var1}pellido del {class_name}: ")
            else:
                name = input(f"\n{var2}ombre {del_dela} {class_name}: ")

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
                if select == 3 and attribute == "apellido":
                    raise ValueError(f"\nEl{var3}apellido del {class_name} no debe contener únicamente espacios vacíos.")
                else:
                    raise ValueError(f"\nEl{var3}nombre {del_dela} {class_name} no debe contener únicamente espacios vacíos.")
            elif only_underscores == True:
                if select == 3 and attribute == "apellido":
                    raise ValueError(f"\nEl{var3}apellido del {class_name} no debe contener únicamente guiones bajos.")
                else:
                    raise ValueError(f"\nEl{var3}nombre {del_dela} {class_name} no debe contener únicamente guiones bajos.")

            for i in name:
               if i.isalpha() == False:
                    if i != " " and i != "_":  
                        if select == 3 and attribute == "apellido":    
                            raise ValueError(f"\nEl{var3}apellido del {class_name} solo puede contener letras, espacios vacíos y guiones bajos.") 
                        else:
                            raise ValueError(f"\nEl{var3}nombre {del_dela} {class_name} solo puede contener letras, espacios vacíos y guiones bajos.")                               

        except ValueError as arg:
            print(arg)
        else:
            break  

    if new == True:    
        while True:
            change_check = str
            if select == 1 and attribute == "director":    
                change_check = input(f"\nConfirme que desea cambiar el nombre del {class_name} del programa de \"{class_instance.principal}\" a \"{name}\" (S/N): ").lower() 
            
            elif select == 3 and attribute == "apellido":
                change_check = input(f"\nConfirme que desea cambiar el apellido del {class_name} de \"{class_instance.last_name}\" a \"{name}\" (S/N): ").lower()

            if change_check == "s":
                if select == 1 and attribute == "director":
                    class_instance.principal = name                                                          
                    print(f"\nEl nuevo nombre del {class_name} del programa es \"{class_instance.principal}\".")

                elif select == 3 and attribute == "apellido":
                    class_instance.last_name = name                                                          
                    print(f"\nEl nuevo apellido  del {class_name} es \"{class_instance.last_name}\".")
                break
            elif change_check == "n":
                if select == 1 and attribute == "director":
                    print(f"\nNo se realizo ningún cambio, el nombre del {class_name} del programa continua siendo \"{class_instance.principal}\".")
                
                elif  select == 3 and attribute == "apellido":
                    print(f"\nNo se realizo ningún cambio, el apellido del {class_name} continua siendo \"{class_instance.last_name}\".")

                break
    else:
        if select == 1 and attribute == "director":
            class_instance.principal = name

        elif  select == 3 and attribute == "apellido":
            class_instance.last_name = name

def name_check_non_existence(clase: str, new = False):
    select = int
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
            if select == 7:
                instance_name = input(f"\n{var1}ombre de la {clase}: ")
            else:
                instance_name = input(f"\n{var1}ombre del {clase}: ")    
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
                if select == 7:
                    raise ValueError(f"\nEl{var2}nombre de la {clase} no debe contener únicamente espacios vacíos.")
                else:
                    raise ValueError(f"\nEl{var2}nombre del {clase} no debe contener únicamente espacios vacíos.")    
            elif only_underscores == True:
                if select == 7:
                    raise ValueError(f"\nEl{var2}nombre de la {clase} no debe contener únicamente guiones bajos.")    
                else:
                    raise ValueError(f"\nEl{var2}nombre del {clase} no debe contener únicamente guiones bajos.")

            for i in instance_name:
                if i.isalnum() == False:
                    if i != " " and i != "_":
                        if select == 7:
                            raise ValueError(f"\nEl{var2}nombre de la {clase} solo puede contener letras, números, espacios vacíos y guiones bajos.") 
                        else:                                        
                            raise ValueError(f"\nEl{var2}nombre del {clase} solo puede contener letras, números, espacios vacíos y guiones bajos.")                                

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

            if instance_check == False:
                if select == 7:
                    raise SyntaxError(f"\nNo existe una {clase} con el nombre \"{instance_name}\".")
                else:

                    raise SyntaxError(f"\nNo existe un {clase} con el nombre \"{instance_name}\".")

        except ValueError as arg:
            print(arg)
        except SyntaxError as arg:
            print(arg)
        else:
            break  

    return instance_name

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
          f"Cantidad de Horas Semanales: {class_instance.week_hours}\n"
          f"Programa en el que esta el Curso: {class_instance.program.program_name}\n"
          f"Precio del Curso: {class_instance.price}\n"
          f"Profesor del Curso: {class_instance.teacher.name} {class_instance.teacher.last_name}\n"
          f"Estatus del Curso: {class_instance.course_status}\n"
          f"Máximo de Estudiantes: {class_instance.max_students}\n"
          f"Mínimo de Estudiantes: {class_instance.min_students}")

def del_instance_in_class(class_instance):
    if type(class_instance) is Program:
        pass
    elif type(class_instance) is Course:
        pass
    elif type(class_instance) is Person:
        pass
    elif type(class_instance) is Classroom:
        pass
    elif type(class_instance) is Building:
        pass
    elif type(class_instance) is Teacher_type:
        pass
    elif type(class_instance) is Turn:
        pass
    elif type(class_instance) is Tuition:
        pass
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return  

    for instance in class_instance.instances:
        if class_instance == instance:
            instance_index = class_instance.instances.index(instance)
            del class_instance.instances[instance_index]

def change_instance_name(class_instance, new_name):
    select = int
    if type(class_instance) is Program:
        select = 1
    elif type(class_instance) is Course:
        select = 2
    elif type(class_instance) is Person:
        select = 3
    elif type(class_instance) is Classroom:
        select = 4
    elif type(class_instance) is Building:
        select = 5
    elif type(class_instance) is Teacher_type:
        select = 6
    elif type(class_instance) is Turn:
        select = 7
    elif type(class_instance) is Tuition:
        select = 8
    else:
        print("\nEl objeto que ingreso no pertenece a ninguna clase válida.") 
        return 

    var = []

    while True:
        change_check = str
        if select == 1:
            change_check = input(f"\nConfirme que desea cambiar el nombre del programa de \"{class_instance.program_name}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 2:
            change_check = input(f"\nConfirme que desea cambiar el nombre del curso de \"{class_instance.course_name}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 3:
            change_check = input(f"\nConfirme que desea cambiar el nombre de la persona de \"{class_instance.name}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 4:
            change_check = input(f"\nConfirme que desea cambiar el nombre del aula de \"{class_instance.classroom_name}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 5:
            change_check = input(f"\nConfirme que desea cambiar el nombre del edificio de \"{class_instance.name}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 6:
            change_check = input(f"\nConfirme que desea cambiar el nombre del tipo de profesor de \"{class_instance.type_teacher}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 7:
            change_check = input(f"\nConfirme que desea cambiar el nombre del turno de \"{class_instance.turn}\" a \"{new_name}\" (S/N): ").lower()
        elif select == 8:
            change_check = input(f"\nConfirme que desea cambiar el nombre de la matricula de \"{class_instance.name}\" a \"{new_name}\" (S/N): ").lower()
        else:
            change_check = "n"

        if change_check == "s":
            locals()[new_name] = copy.deepcopy(class_instance)
            
            if select == 1:
                locals()[new_name].program_name = new_name
            elif select == 2:
                locals()[new_name].course_name = new_name
            elif select == 3 or select == 5 or select == 8:
                locals()[new_name].name = new_name
            elif select == 4:
                locals()[new_name].classroom_name = new_name
            elif select == 6:
                locals()[new_name].type_teacher = new_name
            elif select == 7:
                locals()[new_name].turn = new_name

            for instance in class_instance.__class__.instances:
                if class_instance == instance:
                    instance_index = class_instance.__class__.instances.index(instance)
                    del class_instance.__class__.instances[instance_index]
                                                  
            class_instance.__class__.instances.append(locals()[new_name])

            if select == 1:
                print(f"\nEl nuevo nombre del programa es \"{locals()[new_name].program_name}\".")
            elif select == 2:
                print(f"\nEl nuevo nombre del curso es \"{locals()[new_name].course_name}\".")
            elif select == 3:
                print(f"\nEl nuevo nombre de la persona es \"{locals()[new_name].name}\".")
            elif select == 4:
                print(f"\nEl nuevo nombre del aula es \"{locals()[new_name].classroom_name}\".")
            elif select == 5:
                print(f"\nEl nuevo nombre del edificio es \"{locals()[new_name].name}\".")
            elif select == 6:
                print(f"\nEl nuevo nombre del tipo de profesor es \"{locals()[new_name].type_teacher}\".")
            elif select == 7:
                print(f"\nEl nuevo nombre del turno es \"{locals()[new_name].turn}\".")
            elif select == 8:
                print(f"\nEl nuevo nombre de la matricula es \"{locals()[new_name].name}\".")

            var = [True, locals()[new_name]]
            break
        elif change_check == "n":
            if select == 1:
                print(f"\nNo se realizo ningún cambio, el nombre del programa continua siendo \"{class_instance.program_name}\".")
            elif select == 2:
                print(f"\nNo se realizo ningún cambio, el nombre del curso continua siendo \"{class_instance.course_name}\".")
            elif select == 3:
                print(f"\nNo se realizo ningún cambio, el nombre de la persona continua siendo \"{class_instance.name}\".")
            elif select == 4:
                print(f"\nNo se realizo ningún cambio, el nombre del aula continua siendo \"{class_instance.classroom_name}\".")
            elif select == 5:
                print(f"\nNo se realizo ningún cambio, el nombre del edificio continua siendo \"{class_instance.name}\".")
            elif select == 6:
                print(f"\nNo se realizo ningún cambio, el nombre del tipo de profesor continua siendo \"{class_instance.type_teacher}\".")
            elif select == 7:
                print(f"\nNo se realizo ningún cambio, el nombre del turno continua siendo \"{class_instance.turn}\".")
            elif select == 8:
                print(f"\nNo se realizo ningún cambio, el nombre de la matricula continua siendo \"{class_instance.name}\".")

            var = [False]
            break    

    return var
