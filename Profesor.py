from Tipo_Profesor import TipoProfesor
from Personas import Persona
from Turno import Turno


class Profesor(Persona, TipoProfesor, Turno):
    id = 0

    def __init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email, tipo, turno):
        Profesor.id += 1
        self.id_profesor = Profesor.id
        Persona.__init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email)
        TipoProfesor.__init__(self, tipo)
        Turno.__init__(self, turno)

    def __str__(self):
        return f"""
        Id.{self.id_profesor} = {self.nombre} {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Nacimiento: {self.nacimiento}
        Email: {self.email}
        Tipo: {self.tipo}
        Turno: {self.turno}
    """


if __name__ == '__main__':
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    cedula = input("Ingrese cedula Formato 000-000000-0000A: ")
    direccion = input("Ingrese su Direccion: ")
    telefono = input("Ingrese Su telefono: ")
    nacimiento = input("Ingrese su Fecha de Nacimiento Dia Mes Año: ")
    email = input("Ingrese un email: ")
    tipo = input("Ingrese el Tipo de Profesor: ")
    turno = input("Ingres el Turno del Profesor: ")

    profesor = Profesor(nombre, apellido, cedula, direccion, telefono, nacimiento, email, tipo, turno)
    print(profesor)
#
#     profesor1 = Profesor("Pedro", "Altamirano", "001-121212-10005K", "RepartoSchick", 88997711, "12-12-12",
#                          "Pedroaltamirano@tecnasa.com")
#     profesor2 = Profesor("Maria", "Ordonez", "001-121212-10005K", "RepartoSchick", 88997711, "12-12-12",
#                          "mariaordonez@tecnasa.com")
#     print(profesor1)
#     print(profesor2)
