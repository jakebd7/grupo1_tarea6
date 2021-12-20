#a = {"Matematica": {"Jose": 95, "Roberto": 10, "Juan": 74}, "Robotica": {"Maria": 75, "Miguel": 84, "Esteban": 63, "Timoteo": 49}, "Ingles": {"Jose": 17, "Miguel": 13}}

import copy
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


var1 = input("Introduzca nombre para el objeto de la clase Pru: ")
globals()[var1] = Pru(var1)

var2 = input("2Introduzca nombre para el objeto de la clase Pru: ")
#print(var2.name)

for instance in Pru.instances:
    if globals()[var2] == instance:
        print("Coinciden")

