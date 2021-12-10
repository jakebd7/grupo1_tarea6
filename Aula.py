class Aula:

    def __init__(self, nombre, numero_piso, numero_edificio, capacidad_asientos):
        self.__nombre = nombre
        self.__numero_piso = numero_piso
        self.__numero_edificio = numero_edificio
        self.__capacidad_asientos = capacidad_asientos

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
    def numero_piso(self):
        return self.__numero_piso

    @numero_piso.setter
    def numero_piso(self, numero_piso):
        self.__numero_piso = numero_piso

    @numero_piso.deleter
    def numero_piso(self):
        del self.__numero_piso

    @property
    def numero_edificio(self):
        return self.__numero_edificio

    @numero_edificio.setter
    def numero_edificio(self, numero_edificio):
        self.__numero_edificio = numero_edificio

    @numero_edificio.deleter
    def numero_edificio(self):
        del self.__numero_edificio

    @property
    def capacidad_asientos(self):
        return self.__capacidad_asientos

    @capacidad_asientos.setter
    def capacidad_asientos(self, capacidad_asientos):
        self.__capacidad_asientos = capacidad_asientos

    @capacidad_asientos.deleter
    def capacidad_asientos(self):
        del self.__capacidad_asientos

    def __str__(self):
        return f'''
        Nombre: {self.__nombre}
        Numero de Piso: {self.__numero_piso}
        Numero de Edificio: {self.__numero_edificio} 
        Capacidad de Asientos: {self.__capacidad_asientos}       
        '''
