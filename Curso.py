class Curso:

    def __init__(self, nombre_curso, creditos, cant_hrs_semanales, costo_curso, nota):
        self.__nombre_curso = nombre_curso
        self.__creditos = creditos
        self.__cant_hrs_semanales = cant_hrs_semanales
        self._costo_curso = costo_curso
        self._nota = nota

    @property
    def nombre_curso(self):
        return self.__nombre_curso

    @nombre_curso.setter
    def nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    @nombre_curso.deleter
    def nombre_curso(self):
        del self.__nombre_curso

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos

    @creditos.deleter
    def creditos(self):
        del self.__creditos

    @property
    def cant_hrs_semanales(self):
        return self.__cant_hrs_semanales

    @cant_hrs_semanales.setter
    def cant_hrs_semanales(self, cant_hrs_semanales):
        self.__cant_hrs_semanales = cant_hrs_semanales

    @cant_hrs_semanales.deleter
    def cant_hrs_semanales(self):
        del self.__cant_hrs_semanales

    @property
    def costo_curso(self):
        return self._costo_curso

    @costo_curso.setter
    def costo_curso(self, costo_curso):
        self._costo_curso = costo_curso

    @costo_curso.deleter
    def costo_curso(self):
        del self._costo_curso

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @nota.deleter
    def nota(self):
        del self._nota

    def agregar_curso(self, curso):
        self.__nombre_curso.append(curso)

    def __str__(self):
        return f'''
        Nombre del Curso: {self.__nombre_curso}
        Creditos: {self.__creditos}
        Cantidad de Horas Semanales: {self.__cant_hrs_semanales} 
        Costo de Curso: {self.costo_curso}
        Nota: {self.nota}
        '''
