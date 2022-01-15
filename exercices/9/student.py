class Student:
    __NOMA = 0

    def __init__(self, firstname, surname, birthday, email) -> None:
        self.__firstname = firstname
        self.__surname = surname
        self.__birthday = birthday
        self.__email = email
        self.__noma = Student.__NOMA
        Student.__NOMA += 1

    def __str__(self) -> str:
        return "L'étudiant numéro {} : {} {} né le {}, peut être contacté par {}".format(
            self.__noma,
            self.__firstname,
            self.__surname,
            self.__birthday,
            self.__email
        )
