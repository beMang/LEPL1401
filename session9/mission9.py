### PIECE ###
#############


class Piece:
    def __init__(self, desc: str, p_un: float, p_un_kilo=0, fragile=False, red_tva=False) -> None:
        self.__desc = "{} @ {}".format(desc, p_un)
        self.__p_un = p_un
        self.__p_un_kilo = p_un_kilo
        self.__frag = fragile
        self.__red_tva = red_tva

    def __eq__(self, o) -> bool:
        if type(self) == type(o) and self.__desc == o.description() and self.__p_un == o.prix():
            return True
        else:
            return False

    def description(self):
        return self.__desc

    def prix(self):
        return self.__p_un

    def poids(self):
        return self.__p_un_kilo

    def fragile(self):
        return self.__frag

    def tva_reduit(self):
        return self.__red_tva

###############
### ARTICLE ###
###############


class Article:
    """Cette calsse représente un article de facture simple, avec descriptif et prix

    @author Kim Mens
    @version 4 novembre 2021
    """

    def __init__(self, d, p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix

    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """
        return 0.21   # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

###############
### FACTURE ###
###############


class Facture:
    __next_id = 1
    """
    Cette classe représente une Facture, sous forme d'une liste d'articles.
    """

    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.__id = Facture.__next_id
        Facture.__next_id +=1

    def description(self):
        """
        @post: retourne la description de cette facture.
        """
        return self.__description

    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles:
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Facture No {n} : ".format(n=self.__id) + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
            + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
            + self.barre_str()

    def nombre(self, pce):
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        i = 0
        for a in self.__articles:
            if type(a) == ArticlePiece and a.piece == pce:
                i += a.n
        return i

    def entete_livraison_str(self):
        return "Facture No {n} : ".format(n=self.__id) + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids.pce", "nombre", "poids") \
               + self.barre_str()

    def article_livraison_str(self, art: Piece, n):
        if art.fragile():
            fragile = " (!)"
        else:
            fragile = ""
        description = art.description() + fragile
        poids_t = str(art.poids()*n) + "kg"
        return "| {0:40} | {1:10} | {2:10} | {3:10} |\n".format(description, (str(art.poids())+"kg") , n, poids_t)

    def totaux_livraison_str(self, n, n_tot, poids_tot):
        return self.barre_str() \
            + "| {0:40} | {1:10} | {2:10} | {3:10.2f} |\n".format(str(n) + " articles", "", n_tot, float(poids_tot)) \
            + self.barre_str()

    def print_livraison(self):
        s = self.entete_livraison_str()
        tot_nombre = 0
        tot_poids = 0
        fragile = False
        i=0
        for art in self.__articles:
            if type(art) == ArticlePiece:
                i+=1
                s+=self.article_livraison_str(art.piece, art.n)
                tot_nombre += art.n
                tot_poids += art.n * art.piece.poids()
                if art.piece.fragile:
                    fragile = True
        s+=self.totaux_livraison_str(i, tot_nombre, tot_poids)
        if fragile:
            s += " (!) *** livraison fragile ***"
        return s

#########################
### ARTICLEREPARATION ###
#########################


class ArticleReparation(Article):
    def __init__(self, d: float):
        self.d = d

    def description(self):
        """retourne une description de la réparation

        Returns:
            str: description
        """
        return "Réparation ({h} heures)".format(h=self.d)

    def prix(self):
        return 20 + self.d*35

####################
### ARTICLEPIECE ###
####################


class ArticlePiece(Article):
    def __init__(self, n: int, piece: Piece):
        self.piece = piece
        self.n = n

    def description(self):
        return "{n} * {desc}".format(n=self.n, desc=self.piece.description())

    def prix(self):
        return self.n*self.piece.prix()

    def taux_tva(self):
        if self.piece.tva_reduit() == True:
            return 0.06
        else:
            return 0.21


########################
### RUNNING THE CODE ###
########################

if __name__ == "__main__":
    # Ajouter votre code ici pour imprimer une facture et un borderaux
    # de livraison.
    piece = Piece("Souris gamer ++", 26, 4, True, True)
    piece2 = Piece("blabla", 4, 3, False, False)
    reparation = ArticlePiece(5, piece)
    repar2 = ArticlePiece(8, piece2)
    article = ArticleReparation(5)
    article2 = Article("Téléhpone pour pigeon", 600)

    list = Facture("Petite facture", [reparation, article, article2, repar2])
    print(list.print_livraison())
    print(list)
