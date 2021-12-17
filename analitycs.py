import statistics
from tuition import Tuition
from person import Person

class Analitycs:

    def mean_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print("El estudiante con id {} no tiene nota en el curso {}, por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la media.".format(id_student, course_name))
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            return print("No existe ninguna nota registrada en ningun alumno.")
        else:
            return statistics.mean(list_grades)

    def mode_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print("El estudiante con id {} no tiene nota en el curso {}, por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la moda.".format(id_student, course_name))
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            return print("No existe ninguna nota registrada en ningun alumno.")
        else:
            return statistics.mode(list_grades)

    def median_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print("El estudiante con id {} no tiene nota en el curso {}, por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo de la mediana.".format(id_student, course_name))
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            return print("No existe ninguna nota registrada en ningun alumno.")
        else:
            return statistics.median(list_grades)

    def min_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print("El estudiante con id {} no tiene nota en el curso {}, por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo del mínimo.".format(id_student, course_name))
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            return print("No existe ninguna nota registrada en ningun alumno.")
        else:
            return min(list_grades)

    def max_grades(self):
        list_grades = []
        for course_name in Tuition.instances[0].courses_students:
            for id_student in Tuition.instances[0].courses_students[course_name]:
                if None == Tuition.instances[0].courses_students[course_name][id_student]:
                    print("El estudiante con id {} no tiene nota en el curso {}, por lo tanto, la nota de este curso no sera tomada en cuenta en el cálculo del máximo.".format(id_student, course_name))
                else:
                    list_grades.append(Tuition.instances[0].courses_students[course_name][id_student])

        if list_grades == []:
            return print("No existe ninguna nota registrada en ningun alumno.")
        else:
            return max(list_grades)

    def mean_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print("El estudiante con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la media.".format(student_obj.id_student))
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            return print("No existe ninguna edad de estudiante registrada.")
        else:
            return statistics.mean(list_ages_students)

    def mode_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print("El estudiante con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.".format(student_obj.id_student))
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            return print("No existe ninguna edad de estudiante registrada.")
        else:
            return statistics.mode(list_ages_students)

    def median_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print("El estudiante con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.".format(student_obj.id_student))
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            return print("No existe ninguna edad de estudiante registrada.")
        else:
            return statistics.median(list_ages_students)

    def min_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print("El estudiante con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.".format(student_obj.id_student))
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            return print("No existe ninguna edad de estudiante registrada.")
        else:
            return min(list_ages_students)

    def max_ages_students(self):
        list_ages_students = []
        for student_obj in Person.instances_student:
            if None == student_obj.age:
                print("El estudiante con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.".format(student_obj.id_student))
            else:
                list_ages_students.append(student_obj.age)

        if list_ages_students == []:
            return print("No existe ninguna edad de estudiante registrada.")
        else:
            return max(list_ages_students)

    def mean_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print("El profesor con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la media.".format(teacher_obj.id_teacher))
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            return print("No existe ninguna edad de profesor registrada.")
        else:
            return statistics.mean(list_ages_teachers)


    def mode_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print("El profesor con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.".format(teacher_obj.id_teacher))
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            return print("No existe ninguna edad de profesor registrada.")
        else:
            return statistics.mode(list_ages_teachers)

    def median_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print("El profesor con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.".format(teacher_obj.id_teacher))
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            return print("No existe ninguna edad de profesor registrada.")
        else:
            return statistics.median(list_ages_teachers)

    def min_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print("El profesor con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.".format(teacher_obj.id_teacher))
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            return print("No existe ninguna edad de profesor registrada.")
        else:
            return min(list_ages_teachers)

    def max_ages_teachers(self):
        list_ages_teachers = []
        for teacher_obj in Person.instances_teacher:
            if None == teacher_obj.age:
                print("El profesor con id {} no tiene una edad establecida, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.".format(teacher_obj.id_teacher))
            else:
                list_ages_teachers.append(teacher_obj.age)

        if list_ages_teachers == []:
            return print("No existe ninguna edad de profesor registrada.")
        else:
            return max(list_ages_teachers)

    def mean_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print("El estudiante con id {} no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la media.".format(id_student))
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            return print("No existe ningun crédito registrado en ningun alumno.")
        else:
            return statistics.mean(list_credits)

    def mode_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print("El estudiante con id {} no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la moda.".format(id_student))
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            return print("No existe ningun crédito registrado en ningun alumno.")
        else:
            return statistics.mode(list_credits)

    def median_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print("El estudiante con id {} no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo de la mediana.".format(id_student))
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            return print("No existe ningun crédito registrado en ningun alumno.")
        else:
            return statistics.median(list_credits)

    def min_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print("El estudiante con id {} no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo del mínimo.".format(id_student))
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            return print("No existe ningun crédito registrado en ningun alumno.")
        else:
            return min(list_credits)

    def max_credits_earn(self):
        list_credits = []
        for id_student in Tuition.instances[0].credits_students:
            if None == Tuition.instances[0].credits_students[id_student]:
                print("El estudiante con id {} no tiene creditos ganados, por lo tanto, no sera tomado en cuenta en el cálculo del máximo.".format(id_student))
            else:
                list_credits.append(Tuition.instances[0].credits_students[id_student])

        if list_credits == []:
            return print("No existe ningun crédito registrado en ningun alumno.")
        else:
            return max(list_credits)