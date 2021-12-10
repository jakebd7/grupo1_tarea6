class Turno:

    def __init__(self, turno):
        self.__turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @turno.deleter
    def turno(self):
        del self.__turno

    def __str__(self):
        return f'Turno: {self.turno}'


if __name__ == '__main__':
    turno1 = Turno("Matutino")
    turno2 = Turno("Vespertino")

    print(turno1)
    print(turno2)
