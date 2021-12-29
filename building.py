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
                print(f"\nNo se puede añadir el aula \"{classroom.classroom_name}\" al eficicio \"{self.__name}\", porque ya se encuentra registrada en el edificio \"{building.name}\".")
                return False

        if classroom in self.__classrooms:
            print("\nEl aula ya se encuentra registrada en este edificio.")
            return False
        
        if self.__number_of_classrooms == 0:
            print(f"\nNo se pueden agregar aulas al edificio \"{self.__names}\", porque no ha establecido la cantidad de aulas que tiene el edificio.")
            return False
        elif len(self.__classrooms) <= self.__number_of_classrooms:
            self.__classrooms.append(classroom)
            classroom.building_number = self.__name
            print(f"\nAula \"{classroom.classroom_name}\" añadida exitosamente al edificio \"{self.__name}\".")
            return True
        else:
            print(f"\nNo se pueden añadir mas aulas al edificio \"{self.__name}\". La capacidad máxima de aulas se ha alcanzado previamente.")
            return False

    def __str__(self):
        return "Edificio"