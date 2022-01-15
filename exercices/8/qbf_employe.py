class Employe:
    def __init__(self, nom:str, salaire:float) -> None:
        self.nom = nom
        self.salaire = salaire

    def nom(self):
        return self.nom

    def salaire(self):
        return self.salaire

    def __str__(self) -> str:
        return "{} : {}".format(self.nom, self.salaire)

    def augmente(self, percentage):
        self.salaire*=(1+percentage/100)