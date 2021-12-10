from Personas import Persona


class Estudiante(Persona):
    id = 0

    def __init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email, matricula:bool, total_a_pagar:float):
        Estudiante.id += 1
        self.id_estudiante = Estudiante.id
        Persona.__init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email)
        self.__matricula = matricula
        self.__total_a_pagar = total_a_pagar

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @matricula.deleter
    def matricula(self):
        del self.__matricula\

    @property
    def total_a_pagar(self):
        return self.__total_a_pagar

    @total_a_pagar.setter
    def total_a_pagar(self, total_a_pagar):
        self.__total_a_pagar= total_a_pagar

    @total_a_pagar.deleter
    def total_a_pagar(self):
        del self.__total_a_pagar

    def __str__(self):
        return f"""
        Id.{self.id_estudiante} = {self.nombre} {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Nacimiento: {self.nacimiento}
        Email: {self.email}
        Matricula: {self.matricula}
        Total a Pagar: {self.total_a_pagar}
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
    total_a_pagar = float(input("Ingrese el Pago: "))

    estudiante = Estudiante(nombre, apellido, cedula, direccion, telefono, nacimiento, email, matricula, total_a_pagar)
    print(estudiante)
