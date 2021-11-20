# Programme réalisé  par Adrien Antonutti (NOMA : 3020-21-00) et Louise Buxant (4747-21-00)

# Permet savoir si une chaine de caractère est de l'adn
def is_adn(s):
    valid_character = ["a", "t", "g", "c"]  # Caractère valide
    if not s:
        return False
    else:
        for char in s:
            try:
                # Lance une erreur si le caractère ne se trouve pas dans les caracètres valides
                valid_character.index(char.lower())
            except ValueError:
                return False
        return True

# Retourne le/les index de la position d'une chaîne de caracètre dans une autre (Insensible au majuscule)


def positions(s, p):
    if len(s) < len(p):
        return []
    s = s.lower()  # Pour la sensibilité aux majuscules
    p = p.lower()
    position = []
    # On évite de tout vérifier, on sait que dans les derniers caractères de s, on ne trouvera pas p
    for i in range(len(s) - len(p) + 1):
        if s[i:(i + len(p))] == p:
            position.append(i)
    return position


# Calcul la distance de Hamming entre 2 chaines de caractères de longueurs égales
def distance_h(s1, s2):
    if len(s1) == len(s2):
        distance = 0
        for i in range(len(s1)):
            if s2[i].lower() != s1[i].lower():  # Si caractère différent
                distance += 1
        return distance
    else:
        return None  # Si les 2 chaines de caratères ne sont pas égales


# Renvoie la distance de hamming d'un tableau de chaine de caractère
def distances_matrice(l):
    matrice = []
    for i in l:
        line = []
        for j in l:  # Boucle imbriquée pour parcourir les caractères
            line.append(distance_h(i, j))
        matrice.append(line)
    return matrice
