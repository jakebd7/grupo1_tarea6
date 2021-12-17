__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez'

from classroom import Classroom
from person import Person
from tuition import Tuition
from course import Course
from program import Program
from teacher_type import Teacher_type
from turn import Turn
from building import Building

print("\n         Welcome to the Academic Control System of the Oxford University\n")
student1 = Person.create_person("Student")
student1.min_courses = 2
student1.max_courses = 3
student1.min_courses = 2
student2 = Person.create_person("Student")
student3 = Person.create_person("Student")
student4 = Person.create_person("Student")
student5 = Person.create_person("Student")

profesor_de_planta = Teacher_type("profesor_de_planta")
matutino = Turn("Matutino")

teacher1 = Person.create_person("Teacher")
profesor_de_planta.type_define(teacher1)
matutino.turn_define(teacher1)

print("Tipo Profesor: {}".format(teacher1.teacher_type))
print("Turno Profesor: {}".format(teacher1.turn))

input("Enter")
teacher1.name = "Francisco"
teacher1.min_courses = 2
teacher1.max_courses = 4
teacher1.min_courses = 3



student1.name = "Juan"
student2.name = "Maria"
student3.name = "Hernaldo"
student4.name = "Ricardo"
student5.name = "Pedro"

print("El estudiante 1 es: {}, con id: {}".format(student1.name, student1.id_student))
print("El estudiante 2 es: {}, con id: {}".format(student2.name, student2.id_student))
print("El estudiante 3 es: {}, con id: {}".format(student3.name, student3.id_student))
print("El estudiante 4 es: {}, con id: {}".format(student4.name, student4.id_student))
print("El estudiante 5 es: {}, con id: {}".format(student5.name, student5.id_student))

matematica = Course("matematica")
matematica.price = 50
matematica.max_students = 3
matematica.min_students = 2
matematica.teacher = teacher1
español = Course("español")
español.price = 70
español.max_students = 3
español.min_students = 2
español.teacher = teacher1
robotica = Course("robotica")
robotica.price = 90
robotica.max_students = 3
robotica.min_students = 2
robotica.teacher = teacher1
geografia = Course("geografia")
geografia.price = 120
geografia.max_students = 3
geografia.min_students = 2
geografia.teacher = teacher1
quimica = Course("quimica")
quimica.price = 78
quimica.max_students = 3
quimica.min_students = 2
quimica.teacher = teacher1
ingles = Course("ingles")
ingles.price = 60
ingles.max_students = 3
ingles.min_students = 2
ingles.teacher = teacher1


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
programa1.max_students = 5
programa1.min_students = 2
programa1.add_course(matematica)
programa1.add_course(español)
programa1.add_course(robotica)
programa1.add_course(geografia)
programa1.add_course(quimica)
programa1.add_course(ingles)

matricula = Tuition()

matricula.add_program(programa1, student1)
print(matricula.programs_students)
print("Program1 Status: {}".format(programa1.program_status))

matricula.add_course(matematica, student1)
print("El precio de matematica es: {}".format(matematica.price))
matricula.add_course(robotica, student1)
print("El precio de robotica es: {}".format(robotica.price))
matricula.add_course(español, student1)
print("El precio de español es: {}".format(español.price))
pay = student1.total_cost(matricula)

print("El estudiante 1 debe pagar: {}".format(pay))

matricula.add_note(matematica, student1, 95)
matricula.add_note(español, student1, 90)
matricula.add_note(robotica, student1, 97)

pay = student1.total_cost(matricula)
print("Despues de agregar nota, El estudiante 1 debe pagar: {}".format(pay))

print("Matematica")
aula1 = Classroom("aula1")
aula1.seats_capacity = 10
aula1.add_course(matematica)
edificio1 = Building("edificio1")
edificio1.number_of_classrooms = 20
edificio2 = Building("edificio2")
edificio1.add_classroom(aula1)
edificio1.add_classroom(aula1)
edificio2.add_classroom(aula1)
aula1.add_course(matematica)
aula1.add_course(matematica)


# matricula.add_course(matematica, student2)
# print(matricula.courses_students)
# print("Matematica Status: {}".format(matematica.course_status))
# matricula.add_course(robotica, student2)
#matricula.add_course(ingles, student2)

# matricula.add_course(español, student3)
# matricula.add_course(robotica, student3)

# matricula.add_course(matematica, student3)
# print(matricula.courses_students)
# print("Matematica Status: {}".format(matematica.course_status))
# matricula.add_course(matematica, student4)
# print(matricula.courses_students)
# print("Matematica Status: {}".format(matematica.course_status))
# matricula.add_course(matematica, student5)
# print(matricula.courses_students)
# print("Matematica Status: {}".format(matematica.course_status))

input("pulse enter para continuar")

