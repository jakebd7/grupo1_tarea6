class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, nacimiento, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__nacimiento = nacimiento
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @cedula.deleter
    def cedula(self):
        del self.__cedula

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @telefono.deleter
    def telefono(self):
        del self.__telefono

    @property
    def nacimiento(self):
        return self.__nacimiento

    @nacimiento.setter
    def nacimiento(self, nacimiento):
        self.__nacimiento = nacimiento

    @nacimiento.deleter
    def nacimiento(self):
        del self.__nacimiento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

    def __str__(self):
        return f'[Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, Direccion: {self.direccion}' \
               f'\nTelefono: {self.telefono}, Nacimiento: {self.nacimiento}, Email: {self.email}]'


if __name__ == '__main__':
    persona1 = Persona("Juan", "Perez", "001-181290-10005K", "RepartoSchick", 88997711, "18-12-90", "juanjuarez"
                                                                                                    "@tecnasa.com")

    print(persona1)
