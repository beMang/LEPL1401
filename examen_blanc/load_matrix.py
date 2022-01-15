def load_matrix(filename):
    """
    pre: `filename` est un nom de fichier
    post: retourne une matrice rectangulaire M x N dont le contenu est donné
        dans le fichier `filename`.

    le format du fichier est :
        première ligne : le nombre de lignes M
        deuxième ligne : le nombre de colonnes N
        lignes suivantes : une ligne par élément au format "I,J VAL"
            où 0 <= I < M et 0 <= J < N
            et VAL est le réel en ligne I et colonne J de la matrice

    Les éléments non repris dans le fichier sont initialisés à 0.0.

    En cas d'erreur (exception d'entrée/sortie, fichier non lisible,
    mauvais format) retourne None.
    """
    with open(filename, "r") as f:
        try:
            n_row = int(f.readline())
            n_column = int(f.readline())
            matrix = []

            for i in range(n_row):
                matrix.append([])
                for j in range(n_column):
                    matrix[i].append(0.0)
            
            for line in f.readlines():
                info = line.split()
                number = info[1]
                i,j = info[0].split(",")
                matrix[int(i)][int(j)] = number
            return matrix
        except Exception:
            return None


# TESTS
f = open("mat.txt", "w")
f.write("""\
3
3
0,0 10
1,1 20
0,2 30
""")
f.close()
print(load_matrix("mat.txt"))
