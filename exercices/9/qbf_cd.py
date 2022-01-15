class Item:

    def __init__(self, author, title, serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.__author = author
        self.__title = title
        self.__serial = serial

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [num série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.__serial, self.__author, self.__title)

class CD(Item):
    __next_serial = 100000

    def __init__(self, author, title, duration:int):
        super().__init__(author, title, CD.__next_serial)
        self.__duration = duration
        CD.__next_serial +=1

    def __str__(self):
        return super().__str__() + " ({} s)".format(self.__duration)