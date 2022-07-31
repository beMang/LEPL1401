class SudokuPuzzle:
    def __init__(self, dimension):
        """
        Crée un SudokuPuzzle de dimension `dimension` avec tous les éléments initialisés à 0.
        """
        self.dimension = dimension
        self.carres = [[SudokuCarre(x, y, dimension)
                        for x in range(dimension)]
                       for y in range(dimension)]

    def get_carre(self, x, y):
        """
        Retourne le SudokuCarre qui se trouve à la position (x, y) dans ce Sudoku.
        """
        return self.carres[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le Sudoku.
        """
        s = ""
        for y in range(len(self.carres)):
            for x in range(len(self.carres[y])):
                s += str(self.get_carre(x, y))
            s += "\n"
        return s

    def get_carre_valeurs(self, x, y):
        """
        @pre:  0 ≤ x < N
            0 ≤ y < N
        @post: retourne une liste de toutes les valeurs apparaissant dans le SudokuCarre
            qui se trouve à la position (x, y) du puzzle Sudoku
            Si une valeur apparaît plusieurs fois dans ce carré,
            elle se retrouvera plusieurs fois dans la liste retournée.
        """
        carre = self.carres[x][y]
        lst = []
        for l in carre.cells:
            for v in l:
                lst.append(v)
        return lst

    def get_ligne(self, ligne):
        """
        @pre:  0 ≤ ligne < N x N
        @post: retourne une liste de toutes les valeurs apparaissant
            à une certaine ligne du puzzle Sudoku
            Si une valeur apparaît plusieurs fois sur une ligne
            elle se retrouvera plusieurs fois dans la liste retournée
        """
        lst = []
        line_carre = ligne//self.dimension
        decalage = ligne % self.dimension
        for c in range(self.dimension):
            carre = self.get_carre(c, line_carre)
            for c2 in range(self.dimension):
                lst.append(carre.get_val(c2, decalage))
        return lst

    def get_colonne(self, colonne):
        """
        @pre:  0 ≤ colonne < N x N
        @post: retourne une liste de toutes les valeurs apparaissant
            à une certaine colonne du puzzle Sudoku
            Si une valeur apparaît plusieurs fois sur une colonne
            elle se retrouvera plusieurs fois dans la liste retournée
        """
        lst = []
        line_carre = colonne//self.dimension
        decalage = colonne % self.dimension
        for c in range(self.dimension):
            carre = self.get_carre(line_carre, c)
            for c2 in range(self.dimension):
                lst.append(carre.get_val(decalage, c2))
        return lst

    def is_ordered(self, list):
        for i in range(1, self.dimension+1):
            if list[i-1] != i:
                return False
        return True

    def est_correct(self):    # Ne pas effacer cette ligne
        """
        @pre:  ce Sudoku est bien formé, de dimension self.dimension
        @post: retourne un booléen
            True si le puzzle est correct
            False sinon
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                carre_bool = self.is_ordered(
                    sorted(self.get_carre_valeurs(i, j)))
                column_bool = self.is_ordered(
                    sorted(self.get_colonne(i)))
                line_bool = self.is_ordered(
                    sorted(self.get_ligne(i)))
                if not carre_bool or not column_bool or not line_bool:
                    return False
        return True


class SudokuCarre:

    def __init__(self, x, y, dimension):
        """
        Crée un SudokuCarre de taille `dimension` x `dimension`, avec toutes ses valeurs initialisées à 0.
        """
        self.xcoord_carre = x
        self.ycoord_carre = y
        self.cells = [[0 for x in range(dimension)]
                      for y in range(dimension)]

    def set_val(self, x, y, val):
        """
        Assigne une valeur `val` à la cellule se trouvant à la position (x, y) de ce carré.
        """
        self.cells[y][x] = val

    def get_val(self, x, y):
        """
        Retourne la valeur qui se trouve à la position (x, y) de ce carré.
        """
        return self.cells[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le contenu de ce carré.
        """
        s = "carré (" + str(self.xcoord_carre) + "," + \
            str(self.ycoord_carre) + ") : "
        s += str(self.cells)
        s += " "
        return s


# créer un puzzle Sudoku vide de dimension 2
p = SudokuPuzzle(2)
# remplir les carrés et leurs valeurs
# initiliaser le carré à la position (0,0)
p.get_carre(0, 0).set_val(0, 0, 1)
p.get_carre(0, 0).set_val(1, 0, 4)
p.get_carre(0, 0).set_val(0, 1, 3)
p.get_carre(0, 0).set_val(1, 1, 2)
# initiliaser le carré à la position (1,0)
p.get_carre(1, 0).set_val(0, 0, 3)
p.get_carre(1, 0).set_val(1, 0, 2)
p.get_carre(1, 0).set_val(0, 1, 4)
p.get_carre(1, 0).set_val(1, 1, 1)
# initiliaser le carré à la position (0,1)
p.get_carre(0, 1).set_val(0, 0, 4)
p.get_carre(0, 1).set_val(1, 0, 1)
p.get_carre(0, 1).set_val(0, 1, 2)
p.get_carre(0, 1).set_val(1, 1, 3)
# initiliaser le carré à la position (1,1)
p.get_carre(1, 1).set_val(0, 0, 2)
p.get_carre(1, 1).set_val(1, 0, 3)
p.get_carre(1, 1).set_val(0, 1, 1)
p.get_carre(1, 1).set_val(1, 1, 4)
# imprimer le sudoku
print(p)
# carré (0,0) : [[1, 4], [3, 2]] carré (1,0) : [[3, 2], [4, 1]]
# carré (0,1) : [[4, 1], [2, 3]] carré (1,1) : [[2, 3], [1, 4]]
# ce qui correspond au sudoku suivant :
# 1 4 | 3 2
# 3 2 | 4 1
# ---------
# 4 1 | 2 3
# 2 3 | 1 4


print(p.get_carre_valeurs(0, 1))
print(p.get_ligne(3))
print(p.get_colonne(2))
print(p.est_correct())


def is_ordered(list):
    for i in range(1, 10):
        if list[i-1] != i:
            return False
    return True


def est_correct(self):    # Ne pas effacer cette ligne
    """
    @pre:  ce Sudoku est bien formé, de dimension self.dimension
    @post: retourne un booléen
        True si le puzzle est correct
        False sinon
    """
    for i in range(self.dimension):
        for j in range(self.dimension):
            carre_bool = self.is_ordered(
                sorted(self.get_carre_valeurs(i, j)))
            column_bool = self.is_ordered(
                sorted(self.get_colonne(i)))
            line_bool = self.is_ordered(
                sorted(self.get_ligne(i)))
            if not carre_bool or not column_bool or not line_bool:
                return False
    return True
