import datetime
import time
from Matricula import Matricula
from Curso import Curso
from Programa import Programa
from Estudiante import Estudiante

"""Insercion 1"""
programa_leyes = Programa("Auditoria en Leyes", time.ctime(), "Activo", "Juan Guarnizo")

curso_leyes_1 = Curso("Leyes 1", 3, 40, 150, 90)
curso_leyes_2 = Curso("Leyes 2", 3, 40, 150, 90)
curso_leyes_3 = Curso("Leyes 3", 3, 40, 150, 90)
curso_leyes_4 = Curso("Leyes 4", 3, 40, 150, 90)
curso_leyes_final = Curso("Leyes Final", 1, 40, 150, 90)

matricula1 = Matricula(time.ctime(), time.ctime(), "Auditoria en Leyes")
estudiante1 = Estudiante("Jekson de Jesus", "Pineda Vasquez", "001-180297-1005K", "Managua", 88991269, "12 Feb 1997",
                         "jeksonpineda@gmail.com", True, 150.12)

"""Insercion 2"""
programa_python = Programa("Programacion Python", time.ctime(), "Activo", "Luis Alguera")

curso_python_1 = Curso("Python 1", 3, 45, 180, 95)
curso_python_2 = Curso("Python 2", 3, 45, 180, 95)
curso_python_3 = Curso("Python 3", 3, 45, 180, 95)
curso_python_4 = Curso("Python 4", 3, 45, 180, 95)
curso_python_final = Curso("Python Final", 1, 45, 180, 95)

matricula2 = Matricula(time.ctime(), datetime.time(), "Programacion Python")
estudiante2 = Estudiante("Jason", "Ortiz", "001-121190-5006Q", "Managua", 66998855, "12 Nov 1990,",
                         "jasonortiz@gmail.com", True, 150.12)

"""Insercion 3"""
programa_java = Programa("Programacion Java", time.ctime(), "Activo", "Mario Sanches")

curso_java_1 = Curso("Java 1", 3, 45, 180, 95)
curso_java_2 = Curso("Java 2", 3, 45, 180, 95)
curso_java_3 = Curso("Java 3", 3, 45, 180, 95)
curso_java_4 = Curso("Java 4", 3, 45, 180, 95)
curso_java_final = Curso("Java Final", 1, 45, 180, 95)

matricula3 = Matricula(time.ctime(), time.ctime(), "Programacion Java")
estudiante3 = Estudiante("David", "Weber", "001-121195-5006Q", "Managua", 66998855, "12 Nov 1995,",
                         "davidweber@gmail.com", True, 150.12)


print(matricula1, estudiante1, programa_leyes, curso_leyes_1, curso_leyes_2)  # Insercion 1
print(matricula2, estudiante2, programa_python, curso_python_1, curso_python_2)  # Insercion 2
print(matricula3, estudiante3, programa_java, curso_java_1, curso_java_2)  # Insercion 3
