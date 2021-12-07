class Persona:
    
    def __init__(self, nombre = "None", apellido = "None", cedula = "None", direccion = "None", telefono = "None", fecha_nacimiento = "None", email = "None"):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, value):
        self.__cedula = value

    @cedula.deleter
    def cedula(self):
        del self.__cedula

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @telefono.deleter
    def telefono(self):
        del self.__telefono

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

    @fecha_nacimiento.deleter
    def fecha_nacimiento(self):
        del self.__fecha_nacimiento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email

    def crear_persona(type):
        class Profesor(Persona):
            def __init__(self, nombre = "None", apellido = "None", cedula = "None", direccion = "None", telefono = "None", fecha_nacimiento = "None", email = "None", id_profesor = "None"):
                super(Profesor, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento , email)
                self.__id_profesor = id_profesor

            @property
            def id_profesor(self):
                return self.__id_profesor

            @id_profesor.setter
            def id_profesor(self, value):
                self.__id_profesor = value

            @id_profesor.deleter
            def id_profesor(self):
                del self.__id_profesor

            def crear_profesor(self):
                print("Crear Profesor")

        class Estudiante(Persona):
            def __init__(self, nombre = "None", apellido = "None", cedula = "None", direccion = "None", telefono = "None", fecha_nacimiento = "None", email = "None", id_estudiante = "None"):
                super(Estudiante, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_nacimiento , email)
                self.__id_estudiante = id_estudiante

            
            @property
            def id_estudiante(self):
                return self.__id_estudiante

            @id_estudiante.setter
            def id_estudiante(self, value):
                self.__id_estudiante = value

            @id_estudiante.deleter
            def id_estudiante(self):
                del self.__id_estudiante
            
            def matricular(self):
                print("Placeholder para metodo matricular.")

            def total_a_pagar(self):
                print("Placeholder para metodo total_a_pagar.")

        if (type == "Profesor"):
            return Profesor()
        if (type == "Estudiante"):
            return Estudiante()

persona1 = Persona.crear_persona("Profesor")
print(persona1.nombre)
