import statistics
from tuition import Tuition
from person import Person

class Analitycs:

    def mean_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print(f"\nEl estudiante con id \"{id_student}\" no tiene nota en el curso \"{course_name}\", por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la media.")
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            print("\nNo existe ninguna nota registrada en ningún alumno.")
        else:
            print(f"\nLa media de las notas es: {statistics.mean(list_grades)}")

    def mode_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print(f"\nEl estudiante con id \"{id_student}\" no tiene nota en el curso \"{course_name}\", por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la moda.")
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            print("\nNo existe ninguna nota registrada en ningún alumno.")
        else:
            print(f"\nLa moda de las notas es: {statistics.mode(list_grades)}")

    def median_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print(f"\nEl estudiante con id \"{id_student}\" no tiene nota en el curso \"{course_name}\", por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la mediana.")
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            print("\nNo existe ninguna nota registrada en ningún alumno.")
        else:
            print(f"\nLa mediana de las notas es: {statistics.median(list_grades)}")

    def min_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print(f"\nEl estudiante con id \"{id_student}\" no tiene nota en el curso \"{course_name}\", por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo del mínimo.")
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            print("\nNo existe ninguna nota registrada en ningún alumno.")
        else:
            print(f"\nEl valor mínimo de las notas es: {min(list_grades)}")

    def max_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print(f"\nEl estudiante con id \"{id_student}\" no tiene nota en el curso \"{course_name}\", por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo del máximo.")
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            print("\nNo existe ninguna nota registrada en ningún alumno.")
        else:
            print(f"\nEl valor máximo de las notas es: {max(list_grades)}")

    def mean_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print(f"\nEl estudiante con id \"{student_obj.id_student}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la media.")
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            print("\nNo existe ninguna edad de estudiante registrada.")
        else:
            print(f"\nLa media de las edades de los estudiantes es: {statistics.mean(list_ages_students)}")

    def mode_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print(f"\nEl estudiante con id \"{student_obj.id_student}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.")
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            print("\nNo existe ninguna edad de estudiante registrada.")
        else:
            print(f"\nLa moda de las edades de los estudiantes es: {statistics.mode(list_ages_students)}")

    def median_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print(f"\nEl estudiante con id \"{student_obj.id_student}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.")
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            print("\nNo existe ninguna edad de estudiante registrada.")
        else:
            print(f"\nLa mediana de las edades de los estudiantes es: {statistics.median(list_ages_students)}")

    def min_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print(f"\nEl estudiante con id \"{student_obj.id_student}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.")
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
           print("\nNo existe ninguna edad de estudiante registrada.")
        else:
            print(f"\nEl valor mínimo de las edades de los estudiantes es: {min(list_ages_students)}")

    def max_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print(f"\nEl estudiante con id \"{student_obj.id_student}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.")
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            print("\nNo existe ninguna edad de estudiante registrada.")
        else:
            print(f"\nEl valor máximo de las edades de los estudiantes es: {max(list_ages_students)}")

    def mean_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print(f"\nEl profesor con id \"{teacher_obj.id_teacher}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la media.")
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            print("\nNo existe ninguna edad de profesor registrada.")
        else:
            print(f"\nLa media de las edades de los profesores es: {statistics.mean(list_ages_teachers)}")

    def mode_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print(f"\nEl profesor con id \"{teacher_obj.id_teacher}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.")
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            print("\nNo existe ninguna edad de profesor registrada.")
        else:
            print(f"\nLa moda de las edades de los profesores es: {statistics.mode(list_ages_teachers)}")

    def median_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print(f"\nEl profesor con id \"{teacher_obj.id_teacher}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.")
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            print("\nNo existe ninguna edad de profesor registrada.")
        else:
            print(f"\nLa mediana de las edades de los profesores es: {statistics.median(list_ages_teachers)}")
            statistics.median(list_ages_teachers)

    def min_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print(f"\nEl profesor con id \"{teacher_obj.id_teacher}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.")
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            print("\nNo existe ninguna edad de profesor registrada.")
        else:
            print(f"\nEl valor mínimo de las edades de los profesores es: {min(list_ages_teachers)}")

    def max_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print(f"\nEl profesor con id \"{teacher_obj.id_teacher}\" no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.")
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            print("\nNo existe ninguna edad de profesor registrada.")
        else:
            print(f"\nEl valor máximo de las edades de los profesores es: {max(list_ages_teachers)}")

    def mean_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print(f"\nEl estudiante con id \"{id_student}\" no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la media.")
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            print("\nNo existe ningún crédito registrado en ningún estudiante.")
        else:
            print(f"\nLa media de los creditos ganados por los estudiantes es: {statistics.mean(list_credits)}")

    def mode_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print(f"\nEl estudiante con id \"{id_student}\" no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.")
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            print("\nNo existe ningún crédito registrado en ningún estudiante.")
        else:
            print(f"\nLa moda de los creditos ganados por los estudiantes es: {statistics.mode(list_credits)}")

    def median_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print(f"\nEl estudiante con id \"{id_student}\" no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.")
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            print("\nNo existe ningún crédito registrado en ningún estudiante.")
        else:
            print(f"\nLa mediana de los creditos ganados por los estudiantes es: {statistics.median(list_credits)}")

    def min_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print(f"\nEl estudiante con id \"{id_student}\" no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.")
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            print("\nNo existe ningún crédito registrado en ningún estudiante.")
        else:
            print(f"\nEl valor mínimo de los creditos ganados por los estudiantes es: {min(list_credits)}")

    def max_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print(f"\nEl estudiante con id \"{id_student}\" no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.")
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            print("\nNo existe ningún crédito registrado en ningún estudiante.")
        else:
            print(f"\nEl valor máximo de los creditos ganados por los estudiantes es: {max(list_credits)}")