class Building:
    instances = []

    def __init__(self, name = None, address = None, number_of_floors = None, number_of_classrooms = 0):
        self.__name = name
        self.__address = address
        self.__classrooms = []
        self.__number_of_floors = number_of_floors
        self.__number_of_classrooms = number_of_classrooms
        self.__class__.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @address.deleter
    def address(self):
        del self.__address

    @property
    def number_of_floors(self):
        return self.__number_of_floors

    @number_of_floors.setter
    def number_of_floors(self, value):
        self.__number_of_floors = value

    @number_of_floors.deleter
    def number_of_floors(self):
        del self.__number_of_floors

    @property
    def classrooms(self):
        return self.__classrooms

    @property
    def number_of_classrooms(self):
        return self.__number_of_classrooms

    @number_of_classrooms.setter
    def number_of_classrooms(self, value):
        self.__number_of_classrooms = value
        
    @number_of_classrooms.deleter
    def number_of_classrooms(self):
        del self.__number_of_classrooms

    def add_classroom(self, classroom):
        for building in self.__class__.instances:
            if classroom in building.classrooms:
                return print("No se puede añadir el aula {} al eficicio {}, porque ya se encuentra registrada en el edificio {}".format(classroom.classroom_name, self.__name, building.name))

        if classroom in self.__classrooms:
            return print("El aula ya se encuentra registrada en este edificio.")
        
        if self.__number_of_classrooms == 0:
            return print("No se pueden agregar aulas al edificio {} , porque no ha establecido la cantidad de aulas que tiene el edificio.".format(self.__name))
        elif len(self.__classrooms) <= self.__number_of_classrooms:
            self.__classrooms.append(classroom)
            classroom.building_number = self.__name
            return print("Aula {} añadida exitosamente al edificio {}".format(classroom.classroom_name, self.__name))
        else:
            return print("No se pueden añadir mas aulas al edificio {}. La capacidad máxima de aulas se ha alcanzado previamente.".format(self.__name))

