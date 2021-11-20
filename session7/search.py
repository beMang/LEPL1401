import os.path


def readfile(filename):
    """ Crée une liste des lignes contenues dans un fichier dont le nom est ``filename``

    Args:
        filename: le nom d'un fichier de texte
    Retourne:
        une liste dans laquelle chaque ligne du fichier filename est un élément.
        Si filename n'existe pas, la fonction retourne une liste vide.
    """
    if os.path.isfile(filename):
        with open(filename) as f:
            content = f.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
            return content
    else:
        return []


def get_words(line: str):
    """ pour une chaîne de caractères donnée, retourne une liste des mots dans la chaîne,
        en minuscules, et sans ponctuation, dans l'ordre d'apparence dans le texte.
        Par exemple, pour la chaîne de caractères

        "Turmoil has engulfed the Galactic Republic. The taxation of trade routes
        to outlying star systems is in dispute."

        Le résultat est

        ["turmoil", "has", "engulfed", "the", "galactic", "republic", "the",
        "taxation", "of", "trade", "routes", "to", "outlying", "star", "systems",
        "is", "in", "dispute" ]

        Un caractère est considéré comme une ponctuation si ce n'est pas une
        lettre, selon la fonction string.isalpha () .

    Args:
        line: une chaîne de caractères.
    Retourne:
        une liste des mots dans la chaîne, en minuscules, et sans ponctuation.
    """
    lst = []
    for word in line.split():
        for i in range(len(word)):
            word_without_ponct = ""
            for c in word:
                if c.isalpha():
                    word_without_ponct += c
        if word_without_ponct != "":
            lst.append(word_without_ponct.lower())
    return lst


def create_index(filename):
    """ crée un index pour le fichier avec nom ``filename``. L'index se compose
        d'un dictionnaire dans lequel pour chaque mot du fichier ``filename``
        on retrouve une liste des indices des lignes du fichier qui contiennent
        ce mot.

        Par exemple, pour un fichier avec le contenu suivant:

          While the Congress of the Republic endlessly debates
          this alarming chain of events, the Supreme Chancellor has
          secretly dispatched two Jedi Knights.

        Une partie de l'index, representé comme dictionnaire, est:


          {"while": [0], "the": [0,1], "congress": [0], \
           "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

    Args:
        filename: une chaîne de caractères
    Retourne:
        un dictionnaire avec pour chaque mot du fichier (en minuscules)
        la liste des indices des lignes qui contiennent ce mot.
    """
    index = {}
    lines = readfile(filename)
    for i in range(len(lines)):
        words = get_words(lines[i])
        for w in words:
            if index.get(w) == None:
                index[w] = [i]
            else:
                if i not in index[w]:
                    index[w].append(i)
    return index


def get_lines(words, index):
    """ Détermine les lignes qui contiennent tous les mots indexes dans ``words``,
        selon l'index ``index``.

        Par exemple, pour l'index suivant:

          index = {"while": [0], "the": [0,1], "congress": [0], \
                   "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

        La fonction retourne
          get_lines(["the"]) -> [0,1]
          get_lines(["jedi"]) -> [2]
          get_lines(["the","of"],index) -> [0,1]
          get_lines(["while","the"],index) -> [0]
          get_lines(["congress","jedi"]) -> []
          get_lines(["while","the","congress"]) -> [0]

    Args:
        words: une liste de mots, en minuscules
        index: un dictionnaire contenant pour mots (en minuscules) des listes de nombres entiers
    Retourne:
        une liste des nombres des lignes contenant tous les mots indiqués
    """
    if words:
        searched_lines = index.get(words[0], None)
        if searched_lines != None:
            for word in words:
                word_index = index[word]
                for i in searched_lines:
                    if i not in word_index:
                        searched_lines.remove(i)
            searched_lines.sort()
            return searched_lines
        else:
            return []
    else:
        return []
