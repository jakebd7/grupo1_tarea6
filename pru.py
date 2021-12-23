# #a = {"Matematica": {"Jose": 95, "Roberto": 10, "Juan": 74}, "Robotica": {"Maria": 75, "Miguel": 84, "Esteban": 63, "Timoteo": 49}, "Ingles": {"Jose": 17, "Miguel": 13}}

#import copy
class Pru:
    instances = []

    def __init__(self, name):
        self.__name = name
        self.__class__.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


demo1 = Pru("pedro")

print(f"\nAntes del set: {demo1.name}")

setattr(demo1, "apellido", "juan")

print(f"\nDespues del set: {demo1.name}")


# var1 = input("Introduzca nombre para el objeto de la clase Pru: ")
# globals()[var1] = Pru(var1)

# var2 = input("2Introduzca nombre para el objeto de la clase Pru: ")
# #print(var2.name)

# for instance in Pru.instances:
#     if globals()[var2] == instance:
#         print("Coinciden")

# from teacher_type import Teacher_type

# teacher_1 = Teacher_type("Diurno")
# teacher_2 = Teacher_type("Matutitno")
# teacher_3 = Teacher_type("Vespertino")
# teacher_4 = Teacher_type("Nocturno")

# print("\nMetodo 1")

# # Metodo de acceso 1
# for instance in Teacher_type.instances:
#     """Iterando sobre cada instancia de la clase Teacher_type"""
#     """Imprimir el atributo type_teacher de cada instancia"""
#     print(f"\n{instance.type_teacher}")

# print("\nMetodo 2")

# # Metodo de acceso 2
# for i in range(1,len(Teacher_type.instances),1):
#     """Iterando sobre cada instancia de la clase Teacher_type"""
#     """Imprimir el atributo type_teacher de cada instancia"""
#     print(f"\n{Teacher_type.instances[i].type_teacher}")

# import pru2

# demo1 = input("\nNombrar objeto: ")
# locals()[demo1] = pru2.Pru(demo1)


# print(f"antes de eliminar: {locals()[demo1].name}")
# pru2.check(locals()[demo1])
# print("\nEliminado una ves.")
# print(f"despues de eliminar una vez: {locals()[demo1].name}")
# input("\nPulse enter para continuar.")

# # del locals()[demo1]
# print(f"despues de eliminar 2 veces: {locals()[demo1].name}")
# print("\nEliminado una dos veces.")
# input("\nPulse enter para continuar.")


#print(f"Dentro de pru: {pru2.demo1.name}")

