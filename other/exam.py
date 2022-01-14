def mix(l):    # Ne pas effacer cette ligne
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d’entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    result = []
    for i in range(len(l)//2):
        result.append(l[i])
        result.append(l[len(l)-i-1])
    return result


def acrostiche(file_name):  # Ne pas effacer cette ligne
    """
    @pre:  file_name est le nom d'un fichier de texte
    @post: Retourne une chaîne de caractères contenant la première lettre
          de chaque ligne dans le fichier de texte,
          pour les lignes qui contiennent au moins un caractère.
          Retourne -1 en cas d'erreur d'accès au fichier.
    """
    # à compléter
    try:
        with open(file_name) as f:
            s = ""
            for line in f.readlines():
                s += line[0].strip()
            return s
    except Exception:
        return -1

def gcd(a,b):
    if a>=b:
        min = b
    else:
        min =a
    gcd = 0
    for i in (1, min):
        if a%i==0 and b%i==0:
            gdc = i
    return gdc
