from Personas import Persona
from Programa import Programa
from Matricula import Matricula


class Estudiante(Persona):
    id = 0
    total_pagar = 0

    def __init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email, matricula:bool):
        Estudiante.id += 1
        self.id_estudiante = Estudiante.id
        Persona.__init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email)
        self.__matricula = matricula
        self.total_pagar = 0

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @matricula.deleter
    def matricula(self):
        del self.__matricula

    def total_pagar_m(self):
        if Programa.duracion_programa == 5:
            descuento = Matricula.total_vendido - (0.10 * Matricula.total_vendido)
            return descuento
        elif Programa.duracion_programa.getter == 4:
            descuento = Matricula.total_vendido - (0.05 * Matricula.total_vendido)
            return descuento
        else:
            return Matricula.total_vendido

    def __str__(self):
        # Estudiante.total_pagar(self)
        return f"""\033[93m
        Id.{self.id_estudiante} = {self.nombre} {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Nacimiento: {self.nacimiento}
        Email: {self.email}
        Matricula: {self.matricula}
        Total a Pagar: {self.total_pagar_m()}
        """


if __name__ == '__main__':
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    cedula = input("Ingrese cedula Formato 000-000000-0000A: ")
    direccion = input("Ingrese su Direccion: ")
    telefono = input("Ingrese Su telefono: ")
    nacimiento = input("Ingrese su Fecha de Nacimiento Dia Mes Año: ")
    email = input("Ingrese un email: ")
    matricula = bool(input("Ingrese Estado de la Matricula: "))

    estudiante = Estudiante(nombre, apellido, cedula, direccion, telefono, nacimiento, email, matricula)
    print(estudiante)
