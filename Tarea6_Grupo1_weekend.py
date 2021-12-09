__autor__ = 'David Weeber, Jason Ortiz, Jekson Pineda, Amilcar Ibarra, Leonardo Gonzalez'

from person import Person
from tuition import Tuition
#from course import Course

print("\n         Welcome to the Academic Control System of the Oxford University\n")


student1 = Person.create_person("Student")
student1.name = "Juan"
student1.last_name = "Rodriguez"

tuition_student1 = Tuition()

