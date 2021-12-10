class Programa:

    def __init__(self, nombre_programa, fecha, estado_programa, director):
        self.__nombre_programa = nombre_programa
        self.__fecha = fecha
        self.__estado_programa = estado_programa
        self.__director = director

    @property
    def nombre_programa(self):
        return self.__nombre_programa

    @nombre_programa.setter
    def nombre_programa(self, nombre_programa):
        self.__nombre_programa = nombre_programa

    @nombre_programa.deleter
    def nombre_programa(self):
        del self.__nombre_programa

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @fecha.deleter
    def fecha(self):
        del self.__fecha

    @property
    def estado_programa(self):
        return self.__estado_programa

    @estado_programa.setter
    def estado_programa(self, estado_programa):
        self.__estado_programa = estado_programa

    @estado_programa.deleter
    def estado_programa(self):
        del self.__estado_programa

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @director.deleter
    def director(self):
        del self.__director

    def __str__(self):
        return f'''
        Nombre del Programa: {self.__nombre_programa}
        Fecha de Creacion: {self.__fecha}
        Estado del Programa: {self.__estado_programa} 
        Director: {self.__director}       
        '''
