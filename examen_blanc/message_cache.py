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
                for c in line.strip():
                    if c.isalpha():
                        s+=c
                        break
            return s
    except Exception:
        return -1
