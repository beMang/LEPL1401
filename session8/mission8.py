class Duree:
    def __init__(self, h, m, s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
            m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.h = h
        self.m = m
        self.s = s
        self.correct()

    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        return (self.s + 60*(self.m + self.h*60))

    def delta(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
            et la durée d passée en paramètre.
            Cette valeur renovoyée est positif si cette durée (self)
            est plus gramd que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
            d passée en paramètre; retourne False sinon.
        """
        if self.to_secondes() > d.to_secondes():
            return True
        else:
            return False

    def ajouter(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
            corrigée de manière à ce que les minutes et les secondes soient
            dans l'intervalle [0..60[, en reportant au besoin les valeurs
            hors limites sur les unités supérieures
            (60 secondes = 1 minute, 60 minutes = 1 heure).
            Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        d.correct()
        self.correct()
        total_seconds = self.to_secondes() + d.to_secondes()
        self.h = int(total_seconds//3600)
        total_seconds -= int(self.h*3600)
        self.m = int(total_seconds//60)
        self.s = int(total_seconds - self.m*60)
        self.correct()
    
    def correct(self):
        """Méthode qui corrige les minutes ou secondes en trop
        """
        if self.s >= 60:
            minutes = int(self.s//60)
            self.s -= minutes*60
            self.m += minutes
        elif self.m >=60:
            heures = int(self.m//60)
            self.m -= heures*360
            self.h += heures
        else:
            pass

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)


class Chanson:
    def __init__(self, t, a, d: Duree):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """
        self.title = t
        self.artiste = a
        self.duree = d

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{titre} - {artiste} - {duree}".format(titre=self.title, artiste=self.artiste, duree=self.duree.__str__())


class Album:
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
            et avec une liste de chansons vide.
        """
        self.id = numero
        self.titles = []
        self.duration = Duree(0, 0, 0)

    def add(self, chanson: Chanson):
        if len(self.titles) < 99 and (self.duration.to_secondes() + chanson.duree.to_secondes()) < 75*60:
            self.titles.append(chanson)
            self.duration.ajouter(chanson.duree)
            return True
        else:
            return False

    def __str__(self) -> str:
        content = "Album {num} ({len} chansons, {duree})\n".format(
            num=self.id, len=len(self.titles), duree=self.duration)
        for i in range(len(self.titles)):
            line = "{:02}: {title} - {artiste} - {duration}\n".format(
                i+1, title=self.titles[i].title, artiste=self.titles[i].artiste, duration=self.titles[i].duree
            )
            content += line
        return content


if __name__ == "__main__":
    filename = "music-db.txt"
    with open(filename) as f:
        i = 1
        current_album = Album(i)
        for line in f.readlines():
            info = line.split()
            duree = Duree(0, int(info[2]), int(info[3]))
            song = Chanson(info[0], info[1], duree)
            if not current_album.add(song):
                print(current_album)
                i += 1
                current_album = Album(i)
                current_album.add(song)
        print(current_album)  # on imprime le dernier album
