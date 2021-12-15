__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez'

from person import Person
from tuition import Tuition
from course import Course
from program import Program

print("\n         Welcome to the Academic Control System of the Oxford University\n")

student1 = Person.create_person("Student")
student2 = Person.create_person("Student")
student3 = Person.create_person("Student")
student4 = Person.create_person("Student")

student1.name = "Juan"
student2.name = "Maria"
student3.name = "Hernaldo"
student4.name = "Ricardo"

print("El estudiante 1 es: {}, con id: {}".format(student1.name, student1.id_student))
print("El estudiante 2 es: {}, con id: {}".format(student2.name, student2.id_student))
print("El estudiante 3 es: {}, con id: {}".format(student3.name, student3.id_student))
print("El estudiante 4 es: {}, con id: {}".format(student3.name, student4.id_student))

matematica = Course("matematica")
matematica.price = 50
español = Course("español")
español.price = 70
robotica = Course("robotica")
robotica.price = 90
geografia = Course("geografia")
geografia.price = 120
quimica = Course("quimica")
quimica.price = 78
ingles = Course("ingles")
ingles.price = 60


print("Curso {} creado exitosamente.".format(matematica.course_name))
print("Curso {} creado exitosamente.".format(español.course_name))
print("Curso {} creado exitosamente.".format(robotica.course_name))
print("Curso {} creado exitosamente.".format(geografia.course_name))
print("Curso {} creado exitosamente.".format(quimica.course_name))
print("Curso {} creado exitosamente.".format(ingles.course_name))

input("pulse enter para continuar")

programa1 = Program("Programa 1")
programa1.program_duration = 5
programa1.max_courses = 5
programa1.min_courses = 3
programa1.add_course(matematica)
programa1.add_course(español)
programa1.add_course(robotica)
programa1.add_course(geografia)
programa1.add_course(quimica)
programa1.add_course(ingles)
programa2 = Program("Programa 2")
programa2.program_duration = 4
programa3 = Program("Programa 3")
programa3.program_duration = 6

matricula = Tuition()

matricula.add_program(programa1, student1)
matricula.add_program(programa2, student2)
matricula.add_program(programa3, student3)



matricula.add_course(matematica, student1)
matricula.add_course(español, student1)
matricula.add_course(robotica, student1)

# matricula.add_course(matematica, student2)
# matricula.add_course(robotica, student2)
#matricula.add_course(ingles, student2)

# matricula.add_course(español, student3)
# matricula.add_course(robotica, student3)

input("pulse enter para continuar")

