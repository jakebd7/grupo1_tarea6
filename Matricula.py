import time


class Matricula:
    contador_matricula = 0

    def __init__(self, fecha_matricula, hora_matricula, curso):
        Matricula.contador_matricula += 1
        self.id_matricula = Matricula.contador_matricula
        self.__fecha_matricula = fecha_matricula
        self.__hora_matricula = hora_matricula
        self._curso = list(curso)

    @property
    def fecha_matricula(self):
        return self.__fecha_matricula

    @fecha_matricula.setter
    def fecha_matricula(self, fecha_matricula):
        self.__fecha_matricula = fecha_matricula

    @fecha_matricula.deleter
    def fecha_matricula(self):
        del self.__fecha_matricula

    @property
    def hora_matricula(self):
        return self.__hora_matricula

    @hora_matricula.setter
    def hora_matricula(self, hora_matricula):
        self.__hora_matricula = hora_matricula

    @hora_matricula.deleter
    def hora_matricula(self):
        del self.__hora_matricula

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @curso.deleter
    def curso(self):
        del self._curso

    def agregar_curso(self, curso):
        self._curso.append(curso)

    def __str__(self):
        cursos_str = ''
        for curso in self._curso:
            cursos_str += curso.__str__()

        return f'''\033[92m
        Fecha de la Matricula: {self.__fecha_matricula}
        Hora de la Matricula: {self.__hora_matricula}
        ID: {self.id_matricula}
        Inscripcion: {cursos_str}
        '''


if __name__ == '__main__':
    matricula1 = Matricula(time.ctime(), time.ctime(), "Cursos")
    print(matricula1)
