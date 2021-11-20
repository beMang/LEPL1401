from typing import Iterable
import os.path


def args_numeric(terms: Iterable):
    """Vérifie si une liste est uniquement numérique (entière)

    Args:
        terms (Iterable): liste à vérifier

    Returns:
        bool: True si uniquement numérique
                False si pas
    """
    for i in range(len(terms)):
        if terms[i].isdigit():
            pass
        else:
            return False
    return True


def sum(terms: Iterable):
    """Somme les termes d'une suite (numérique)

    Args:
        terms (Iterable): la liste de nombre

    Returns:
        float: la somme des nombres
    """
    sum = 0.0
    for i in terms:
        sum += float(i)
    return sum


def average(terms: Iterable):
    """Calcule la moyenne arithmétique d'une suite

    Args:
        terms (Iterable): la suite de nombre

    Returns:
        float: la moyenne arithmétique
    """
    return sum(terms)/len(terms)


def help():
    """Renvoie l'aide pour utiliser le programme

    Returns:
        str: le contenu de la documentation du programme
    """
    f = open("./session6/README.txt",
             "r")  # Pour écrire l'aide dans un autre fichier
    content = f.read()
    f.close()
    return content


def file_info(filename: str):
    """renvoie le nombre de ligne et de caractère d'un fichier

    Args:
        filename (str): nom du fichier

    Returns:
        tuple: (nbr de ligne, nbr de caractère)
    """
    file = open(filename)
    number_line = 0
    number_char = 0
    for line in file:
        number_line += 1
        number_char += len(line)
    file.close()
    return (number_line, number_char)


def dictionnary(filename):
    """renvoie une liste de tupple trié à partir d'un fichier dictionnaire

    Args:
        filename (str): nom du fichier

    Raises:
        ValueError: si le dictionnaire n'a pas le bon format

    Returns:
        list: la liste des tupple (word, occurence) ordonnées par ordre alphabétique
    """
    file = open(filename)
    dictionnary = []
    for line in file:
        # On met un maxsplits pour être sur du format (mot,occurence)
        info = line.split(",", 1)
        if len(info) != 2:
            raise ValueError("Le dictionnaire n'a pas le bon format")
        else:
            if not info[1].strip().isdigit():
                raise ValueError("Le dictionnaire n'a pas le bon format")
            else:
                dictionnary.append((info[0].strip(), info[1].strip()))
    file.close()
    # On trie pour chercher plus rapidement après
    dictionnary = sorted(dictionnary, key=lambda dictionnary: dictionnary[0])
    return dictionnary


def search(dictionnary, s):
    """Recherche (binaire) des éléments dans un dictionnaire (word, occurence)

    Args:
        dictionnary (list[(word, occurence)]): le dictionnaire dans lequel chercher
        s (str): l'élément à chercher

    Returns:
        tupple|bool: (word, occurence) si le mot est trouvé, False sinon
    """
    first = 0
    last = len(dictionnary) - 1
    found = False
    s = s.strip()  # Pour enlever espace en trop si jamais

    while first <= last and not found:
        middle = (first+last)//2
        if dictionnary[middle][0] == s:
            found = dictionnary[middle]
        else:
            if dictionnary[middle][0] < s:
                first = middle + 1
            else:
                last = middle-1

    return found


# Variables de l'état de l'outil
current_file = None
current_dictionnary = None
continue_program = True

# Boucle principale
while continue_program:
    command = input("> ")
    command = command.split()
    args = command.copy()
    args.remove(command[0])  # Retire la commande principale des
    if command[0] == "exit":
        continue_program = False
    elif command[0] == "sum":
        # Vérifie que les arguments sont corrects
        if args and args_numeric(args):
            print("La somme de ces nombres est : ", sum(args))
        else:
            print("Arguments invalides pour la somme")
    elif command[0] == "avg":
        if args and args_numeric(args):
            print("La moyenne de ces nombres est : ", average(args))
        else:
            print("Arguments invalides pour la moyenne")
    elif command[0] == "help":
        print(help())
    elif command[0] == "info":
        if current_file:
            info = file_info(current_file)
            print(info[0], " lignes")
            print(info[1], "caractères")
        else:
            print("Pas de fichier sélectionné")
    elif command[0] == "dictionnary":
        if current_file:
            try:
                current_dictionnary = dictionnary(current_file)
            except ValueError as err:  # Attrape les exceptions
                print(err)
        else:
            print("Pas de fichier sélectionner, impossible d'activer le dictionnaire")
    elif command[0] == "search":
        if current_dictionnary:
            if len(args) == 1:
                result = search(current_dictionnary, args[0])
                if result == False:
                    print(args[0], " n'est pas dans le dictionnaire")
                else:
                    print(result[0], " est dans le dictionnaire et a",
                          result[1], " occurences.")
            else:
                print("Argument invalide pour la recherche")
        else:
            print("Pas de dictionnaire sélectionné")
    elif command[0] == "file":
        # On vérifie que le fichier existe
        if args and os.path.isfile(args[0]):
            current_file = args[0]
            current_dictionnary = None  # On réinitialise le dictionnaire
            print("File ", current_file, " loaded")
        else:
            print("Fichier inconnu")
    else:
        print("Commande inconnue")
