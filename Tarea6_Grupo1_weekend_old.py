__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez'

from classroom import Classroom
from person import Person
from tuition import Tuition
from course import Course
from program import Program
from teacher_type import Teacher_type
from turn import Turn
from building import Building
from analitycs import Analitycs

print("\n         Welcome to the Academic Control System of the Oxford University\n")
student1 = Person.create_person("Student")
student1.min_courses = 2
student1.max_courses = 3
student1.min_courses = 2
student2 = Person.create_person("Student")
student2.min_courses = 2
student2.max_courses = 3
student2.min_courses = 2
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

teacher2 = Person.create_person("Teacher")
profesor_de_planta.type_define(teacher2)
matutino.turn_define(teacher2)

print("Tipo Profesor: {}".format(teacher2.teacher_type))
print("Turno Profesor: {}".format(teacher2.turn))

input("Enter")
teacher1.name = "Francisco"
teacher1.min_courses = 2
teacher1.max_courses = 4
teacher1.min_courses = 3
teacher1.age = 25

teacher2.name = "Mario"
teacher2.min_courses = 2
teacher2.max_courses = 4
teacher2.min_courses = 3
teacher2.age = 70

student1.name = "Juan"
student1.age = 30
student2.name = "Maria"
student2.age = 60
student3.name = "Hernaldo"
student4.name = "Ricardo"
student4.age = 40
student5.name = "Pedro"
student5.age = 36

print("El estudiante 1 es: {}, con id: {}".format(student1.name, student1.id_student))
print("El estudiante 2 es: {}, con id: {}".format(student2.name, student2.id_student))
print("El estudiante 3 es: {}, con id: {}".format(student3.name, student3.id_student))
print("El estudiante 4 es: {}, con id: {}".format(student4.name, student4.id_student))
print("El estudiante 5 es: {}, con id: {}".format(student5.name, student5.id_student))

matematica = Course("matematica")
matematica.price = 50
matematica.max_students = 3
matematica.min_students = 2
matematica.credits = 3
matematica.teacher = teacher1
español = Course("español")
español.price = 70
español.max_students = 3
español.min_students = 2
español.credits = 2
español.teacher = teacher1
robotica = Course("robotica")
robotica.price = 90
robotica.max_students = 3
robotica.min_students = 2
robotica.credits = 4
robotica.teacher = teacher1
geografia = Course("geografia")
geografia.price = 120
geografia.max_students = 3
geografia.min_students = 2
geografia.credits = 2
geografia.teacher = teacher1
quimica = Course("quimica")
quimica.price = 78
quimica.max_students = 3
quimica.min_students = 2
geografia.credits = 3
quimica.teacher = teacher1
ingles = Course("ingles")
ingles.price = 60
ingles.max_students = 3
ingles.min_students = 2
ingles.price = 3
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

matricula.add_program(programa1, student2)

matricula.add_course(matematica, student1)
print("El precio de matematica es: {}".format(matematica.price))
matricula.add_course(robotica, student1)
print("El precio de robotica es: {}".format(robotica.price))
matricula.add_course(español, student1)
print("El precio de español es: {}".format(español.price))
pay = student1.total_cost(matricula)

matricula.add_course(matematica, student2)
matricula.add_course(ingles, student2)
matricula.add_course(geografia, student2)


print("El estudiante 1 debe pagar: {}".format(pay))

matricula.add_note(matematica, student1, 95)
matricula.add_note(español, student1, 90)
matricula.add_note(robotica, student1, 59)

matricula.add_note(matematica, student2, 70)
matricula.add_note(ingles, student2, 25)
matricula.add_note(geografia, student2, 80)

pay = student1.total_cost(matricula)

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

analisis = Analitycs()

mean_grades = analisis.mean_grades()
print("La media de las notas es: {}".format(mean_grades))
mode_grades = analisis.mode_grades()
print("La moda de las notas es: {}".format(mode_grades))
median_grades = analisis.median_grades()
print("La mediana de las notas es: {}".format(median_grades))
min_grades = analisis.min_grades()
print("El mínimo de las notas es: {}".format(min_grades))
max_grades = analisis.max_grades()
print("El máximo de las notas es: {}".format(max_grades))

mean_ages_students = analisis.mean_ages_students()
print("La media de la edad de los estudiantes es: {}".format(mean_ages_students))
# mode_ages_students = analisis.mode_ages_students()
# print("La moda de la edad de los estudiantes es: {}".format(mode_ages_students))
# median_ages_students = analisis.median_ages_students()
# print("La mediana de la edad de los estudiantes es: {}".format(median_ages_students))
# min_ages_students = analisis.min_ages_students()
# print("El mínimo de la edad de los estudiantes es: {}".format(min_ages_students))
# max_ages_students = analisis.max_ages_students()
# print("El máximo de la edad de los estudiantes es: {}".format(max_ages_students))

mean_ages_teachers = analisis.mean_ages_teachers()
print("La media de la edad de los profesores es: {}".format(mean_ages_teachers))
mode_ages_teachers = analisis.mode_ages_teachers()
print("La moda de la edad de los profesores es: {}".format(mode_ages_teachers))
median_ages_teachers = analisis.median_ages_teachers()
print("La mediana de la edad de los profesores es: {}".format(median_ages_teachers))
min_ages_teachers = analisis.min_ages_teachers()
print("El mínimo de la edad de los profesores es: {}".format(min_ages_teachers))
max_ages_teachers = analisis.max_ages_teachers()
print("El máximo de la edad de los profesores es: {}".format(max_ages_teachers))

mean_credits_earn = analisis.mean_credits_earn()
print("La media de los creditos ganados es: {}".format(mean_credits_earn))
mode_credits_earn = analisis.mode_credits_earn()
print("La moda de los creditos ganados es: {}".format(mode_credits_earn))
median_credits_earn = analisis.median_credits_earn()
print("La mediana de los creditos ganados es: {}".format(median_credits_earn))
min_credits_earn = analisis.min_credits_earn()
print("El mínimo de los creditos ganados es: {}".format(min_credits_earn))
max_credits_earn = analisis.max_credits_earn()
print("El máximo de los creditos ganados es: {}".format(max_credits_earn))

# matricula.add_course(matematica, student2)
# print(matricula.courses_students)
# print("Matematica Status: {}".format(matematica.course_status))
# matricula.add_course(robotica, student2)
# matricula.add_course(ingles, student2)

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

