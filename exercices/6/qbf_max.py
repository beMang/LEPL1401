def get_max(filename):
    """
        pre:    filename est une chaîne de caractères
        post:   Renvoie le plus grand nombre réel >= 0 trouvé dans le fichier de nom
                filename.
                Les lignes ne représentant pas un seul nombre réel >= 0 sont ignorées.
                Si le fichier n'existe pas ou si une erreur d'entrée/sortie survient,
                la fonction renvoie la valeur -1, et imprime un message d'erreur.
                Si le fichier ne contient aucune ligne valide, renvoie
                la valeur -1.

                Par exemple, la méthode retourne 10.0 pour le fichier de contenu suivant:
                0.345.67
                hello
                -543.0
                500.0 1000.0 2000.0
                10.0
                3.1416
    """
    try:
        f = open(filename, "r")
        max = -1
        for line in f.readlines():
            try:
                if float(line) >=0 and float(line)>=max:
                    max = float(line)
            except Exception:
                pass
        f.close()
        return max
    except Exception:
        return -1