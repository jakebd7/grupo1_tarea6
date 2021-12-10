from Profesor import *
import datetime
import time
from Matricula import Matricula
from Curso import Curso
from Programa import Programa
from Estudiante import Estudiante

"""Reglas de Negocio - Valores Constantes"""
try:

    cursos_max_programa = int(input("Ingrese Cuantos es el Maximo de Cursos para un Programa: "))
    cursos_min_programa = int(input("Ingrese Cuantos es el Minimo de Cursos para un Programa: "))

    estudiante_max_programa = int(input("Ingrese Cuantos es el Maximo de Programas para un Estudiante: "))
    estudiante_min_programa = int(input("Ingrese Cuantos es el Minimo de Programas para un Estudiante: "))

    profesor_max_cursos = int(input("Ingrese Cuantos es el Maximo de Cursos a impartir para un Profesor: "))
    profesor_min_cursos = int(input("Ingrese Cuantos es el Minimo de Cursos a impartir para un Profesor: "))

    # min_estudiante_para_abrir_programa = int(input("Ingrese el minimo de estudiantes para abrir un Programa: "))
    # max_estudiante_para_abrir_programa = int(input("Ingrese el maximo de estudiantes para abrir un Programa: "))
    #
    # min_estudiante_para_abrir_curso = int(input("Ingrese el minimo de estudiantes para abrir un curso: "))
    # max_estudiante_para_abrir_curso = int(input("Ingrese el maximo de estudiantes para abrir un curso: "))

    """Programa, Profesor y Curso 1"""
    programa_leyes = Programa("Auditoria en Leyes", time.ctime(), "Activo", "Juan Guarnizo")
    profesor_curso_leyes = Profesor("Mario Jose", "Dolores Estrada", "001-121212-1225L", "Masatepe", 88997744,
                                    "12 Dic 2012","josedolroes@gmail.com", "Planta", "Matutino")
    curso_leyes_1 = Curso("Leyes 1", 3, 40, 150, 90)
    curso_leyes_2 = Curso("Leyes 2", 3, 40, 150, 90)
    curso_leyes_3 = Curso("Leyes 3", 3, 40, 150, 90)
    curso_leyes_4 = Curso("Leyes 4", 3, 40, 150, 90)
    curso_leyes_final = Curso("Leyes Final", 1, 40, 150, 90)

    """Programa, Profesor y Curso 2"""
    programa_python = Programa("Programacion Python", time.ctime(), "Activo", "Luis Alguera")
    profesor_curso_python = Profesor("Luisa Marbelly", "Ramirez Gollena", "001-121212-1225L", "Masatepe", 88997744,
                                     "12 Dic 2012", "luisagollena@gmail.com", "Planta", "Matutino")
    curso_python_1 = Curso("Python 1", 3, 45, 180, 95)
    curso_python_2 = Curso("Python 2", 3, 45, 180, 95)
    curso_python_3 = Curso("Python 3", 3, 45, 180, 95)
    curso_python_4 = Curso("Python 4", 3, 45, 180, 95)
    curso_python_final = Curso("Python Final", 1, 45, 180, 95)

    """Programa, Profesor y Curso 3"""
    programa_java = Programa("Programacion Java", time.ctime(), "Activo", "Mario Sanches")
    profesor_curso_java = Profesor("Francisco Mora", "Gutierre Urbina", "001-121212-1225L", "Masatepe", 88997744,
                                   "12 Dic 2012","franurbina@gmail.com", "Parcial", "Matutino")
    curso_java_1 = Curso("Java 1", 3, 45, 180, 95)
    curso_java_2 = Curso("Java 2", 3, 45, 180, 95)
    curso_java_3 = Curso("Java 3", 3, 45, 180, 95)
    curso_java_4 = Curso("Java 4", 3, 45, 180, 95)
    curso_java_final = Curso("Java Final", 1, 45, 180, 95)

    """Creacion de Estudiantes"""
    estudiante1 = Estudiante("Jekson de Jesus", "Pineda Vasquez", "001-180297-1005K", "Managua", 88991269, "12 Feb 1997",
                             "jeksonpineda@gmail.com", True, 150.12)
    estudiante2 = Estudiante("Jason", "Ortiz", "001-121190-5006Q", "Managua", 66998855, "12 Nov 1990,",
                             "jasonortiz@gmail.com", True, 150.12)
    estudiante3 = Estudiante("David", "Weber", "001-121195-5006Q", "Managua", 66998855, "12 Nov 1995,",
                             "davidweber@gmail.com", True, 150.12)

    """Creacion de Matriculas"""
    matricula1 = Matricula(time.ctime(), time.ctime(), "Auditoria en Leyes")
    matricula2 = Matricula(time.ctime(), datetime.time(), "Programacion Python")
    matricula3 = Matricula(time.ctime(), time.ctime(), "Programacion Java")

    if cursos_min_programa <= Programa.id_programa <= cursos_max_programa:
        if estudiante_min_programa <= Estudiante.id <= estudiante_max_programa:
            if profesor_min_cursos <= Profesor.id_profesor <= profesor_max_cursos:
                print(matricula1, estudiante1, programa_leyes, curso_leyes_1, curso_leyes_2,
                      profesor_curso_leyes)  # Insercion 1
                print(matricula2, estudiante2, programa_python, curso_python_1, curso_python_2,
                      profesor_curso_python)  # Insercion 2
                print(matricula3, estudiante3, programa_java, curso_java_1, curso_java_2,
                      profesor_curso_java)  # Insercion 3

                print(matricula1, estudiante1, programa_python, curso_python_1, curso_python_2, programa_python,
                      profesor_curso_python)  # Insercion 4
                print(matricula1, estudiante1, programa_java, curso_java_1, curso_java_2,
                      profesor_curso_java)  # Insercion 5
            else:
                print("Error en la cantidad de Cursos para un Profesor")
        else:
            print("Error en la cantidad de Programas para un Estudiante")
    else:
        print("Error en la cantidad de Cursos para un Programa")

except ValueError:
    print("Ingreso algun Dato Incorrectamente")
except NameError:
    print("Valores No leido")