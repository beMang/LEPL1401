class Student:

    def __init__(self, n):
        """
        Initialise un nouvel objet de type Student avec un nom n donné.
        @pre:  -
        @post: Un objet de type Student a été créé avec comme 'name' n,
               et un score None pour chacun des trois tests 'test1', 'test2' et 'test3'
        """
        # nom de l'étudiant
        self.name = n
        # score reçu par l'étudiant sur trois tests
        # (initialement None car l'étudiant n'a pas encore passé les tests)
        self.test1 = None
        self.test2 = None
        self.test3 = None

    def average_score(self):
        """"
        Calcul du score moyen que l'étudiant a obtenu sur les 3 tests.
        @pre: les variables d'instance test1, test2 et test3
              contiennent des valeurs de type int
        @post: retourne la valeur moyenne de ces trois valeurs
        """
        return (self.test1 + self.test2 + self.test3) / 3

    def __str__(self) -> str:
        content = "Bonjour, " + self.name + ". Vos scores sont:\n"
        content += str(self.test1) + "\n"
        content += str(self.test2) + "\n"
        content += str(self.test3) + "\n"
        content+="Votre score moyenne est " + str(self.average_score())
        return content

s = Student("Adrien")
s.test1 = 10
s.test2 = 3
s.test3 = 5

print(s)
