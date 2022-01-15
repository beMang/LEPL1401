class Animal:
    def __init__(self, name, diurnal=None, legs=None) -> None:
        self.name = name
        self.diurnal = diurnal
        self.nb_legs = legs
        self.asleep = False

    def sleep(self):
        if self.asleep == True:
            raise RuntimeError("Dors déjà")
        else:
            self.asleep = True

    def wake_up(self):
        if self.asleep == False:
            raise RuntimeError("Déjà réveillé")
        else:
            self.asleep = False


class Lion(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, True, 4)

    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, False, 2)

    def fly():
        pass


class Giraffe(Animal):
    def __init__(self, name, neck) -> None:
        super().__init__(name, True, 4)
        if (type(neck) != int and type(neck) != float) or neck < 0:
            raise ValueError("Taille du cou impossible")
        else:
            self.neck_length = neck


class Zoo:
    def __init__(self) -> None:
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Pas un animal")
        else:
            self.animals.append(animal)


def create_my_zoo():
    zoo = Zoo()
    animals = [
        Lion("Simba"),
        Owl("Chouette"),
        Giraffe("Petit cou", 1),
        Giraffe("Ultra-cou", 50)
    ]
    for a in animals:
        zoo.add_animal(a)
    return zoo
