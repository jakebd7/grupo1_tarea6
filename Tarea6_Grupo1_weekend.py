__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez'

from person import Person
from tuition import Tuition
from course import Course

print("\n         Welcome to the Academic Control System of the Oxford University\n")


student1 = Person.create_person("Student")
input("pulse enter para continuar")
student2 = Person.create_person("Student")
input("pulse enter para continuar")
student3 = Person.create_person("Student")

student1.name = "Juan"
student2.name = "Maria"
student3.name = "Hernaldo"

print("El estudiante 1 es: {}, con id: {}".format(student1.name, student1.id_student))
print("El estudiante 2 es: {}, con id: {}".format(student2.name, student2.id_student))
print("El estudiante 3 es: {}, con id: {}".format(student3.name, student3.id_student))

matematica = Course("matematica")
matematica.price = 50
español = Course("español")
español.price = 70
robotica = Course("robotica")
robotica.price = 90

print("Curso {} creado exitosamente.".format(matematica.course_name))
print("Curso {} creado exitosamente.".format(español.course_name))
print("Curso {} creado exitosamente.".format(robotica.course_name))

input("pulse enter para continuar")

matricula = Tuition()

matricula.add_course(matematica, student1)
matricula.add_course(español, student1)
matricula.add_course(robotica, student1)

matricula.add_course(matematica, student2)
matricula.add_course(robotica, student2)

matricula.add_course(español, student3)
matricula.add_course(robotica, student3)

print(matricula.courses_students)

venta = matricula.total_fee()

print("Total Vendido: {}".format(venta))


input("pulse enter para continuar")

