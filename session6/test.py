from assistant import *

# Différents tests pour les méthodes de l'assistant, basée sur les fichiers "error1.dat" et "error2.dat"


def tests_args_numeric():
    numeric_suit = ["4", "5", "9"]
    no_numeric_suit = ["1", "B", "3"]
    assert args_numeric(numeric_suit) == True
    assert args_numeric(no_numeric_suit) == False


def test_sum():
    assert float((5+5+6)) == sum([5,5,6])


def test_average():
    array = [5, 5, 6]
    assert sum(array)/3 == average(array)


def test_file_info():
    info = file_info("error1.dat")
    assert info[0] == 5
    assert info[1] == 51


def test_dictionnary():
    """Test la fonction "dictionnary"

        Attrape les erreurs et vérifie le message pour être sur que la fonction se comporte comme prévu

    Raises:
        RuntimeError: si le fichier considérer valide est invalide
    """
    try:
        dictionnary("error1.dat")
    except ValueError as err:
        assert err.__str__() == "Le dictionnaire n'a pas le bon format"
    try:
        dictionnary("error2.dat")
    except ValueError as err:
        assert err.__str__() == "Le dictionnaire n'a pas le bon format"
    try:
        valid_dictionnary = dictionnary("all-words.dat")
        assert type(valid_dictionnary) == list
    except ValueError as err:
        raise RuntimeError("Erreurs dans les tests")


def test_search():
    valid_dictionnary = [("bonjour", 4), ("hello", 6), ("python", 90)]
    assert search(valid_dictionnary, "bonjour") == valid_dictionnary[0]
    assert search(valid_dictionnary, "random") == False


def run_tests():
    """Méthode pour lancer tous les tests facilement
    """
    tests_args_numeric()
    test_sum()
    test_average()
    test_file_info()
    test_dictionnary()
    test_search()


run_tests()
