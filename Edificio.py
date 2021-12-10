class Edificio:

    def __init__(self, nombre, direccion, cantidad_pisos, cantidad_aulas):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_aulas = cantidad_aulas

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
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def cantidad_pisos(self):
        return self.__cantidad_pisos

    @cantidad_pisos.setter
    def cantidad_pisos(self, cantidad_pisos):
        self.__cantidad_pisos = cantidad_pisos

    @cantidad_pisos.deleter
    def cantidad_pisos(self):
        del self.__cantidad_pisos

    @property
    def cantidad_aulas(self):
        return self.__cantidad_aulas

    @cantidad_aulas.setter
    def cantidad_aulas(self, cantidad_aulas):
        self.__cantidad_aulas = cantidad_aulas

    @cantidad_aulas.deleter
    def cantidad_aulas(self):
        del self.__cantidad_aulas

    def __str__(self):
        return f'''
        Nombre: {self.__nombre}
        Direccion: {self.__direccion}
        Cantidad de Pisos: {self.__cantidad_pisos} 
        Cantidad de Aulas: {self.__cantidad_aulas}       
        '''
