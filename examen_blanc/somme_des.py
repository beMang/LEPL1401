def somme_des(n):
    """
    @pre:  n est un nombre entier > 0
    @post: retourne un dictionnaire avec comme différentes clés
           chaque somme possible des valeurs des dés,
           et comme valeur associée à cette clé e,
           la liste des tuples des valeurs des dés qui addtionnées donnent e
    """
    d={}
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d.get(i+j):
                d[i+j].append((i,j))
            else:
                d[i+j] = [(i,j)]
    return d