class Pru:
    instances = []

    def __init__(self, name = None):
        self.name = name
        Pru.instances.append(self)
        print("Creado estudidante No.{}".format(len(Pru.instances)))
        print("Instancias creadas: {}".format(Pru.instances))

a = Pru("Juan")
input()
b = Pru("Maria")
input()
c = Pru("Roberto")

print(len(Pru.instances))