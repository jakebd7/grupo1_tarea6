class TipoProfesor:
    def __init__(self, tipo):
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @tipo.deleter
    def tipo(self):
        del self.__tipo

    def __str__(self):
        return f'Tipo: {self.tipo}'


if __name__ == '__main__':
    tipo1 = TipoProfesor("Planta")
    tipo2 = TipoProfesor("Parcial")

    print(tipo1)
    print(tipo2)
