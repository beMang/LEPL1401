from mission8 import Duree, Chanson, Album
##############################
# Tests pour la classe Duree #
##############################

d0 = Duree(0, 0, 0)
d1 = Duree(10, 20, 59)
d2 = Duree(8, 41, 25)


def test_Duree_str():
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"


def test_Duree_to_secondes():
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"


def test_Duree_delta():
    assert d0.delta(d1) == - d1.to_secondes()
    assert d1.delta(d0) == d1.to_secondes()
    assert d1.delta(d2) == d1.to_secondes() - d2.to_secondes()


def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    assert d2.apres(d0)


def test_Duree_ajouter():
    d1.ajouter(d0)
    assert d1.to_secondes() == 37259
    d2.ajouter(d1)
    assert d2.to_secondes() == 37259 + 31285


# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

title = "Let's Dance"
artiste = "David Bowie"
duree = Duree(0, 4, 5)
c = Chanson(title, artiste, duree)


def test_chanson_creation():
    assert title == c.title
    assert artiste == c.artiste
    assert duree == c.duree


def test_Chanson_str(chanson: Chanson):
    assert str(chanson) == "Let's Dance - David Bowie - " + str(chanson.duree)


# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)
test_chanson_creation()

##############################
# Tests pour la classe Album #
##############################

a = Album(4)


def test_album_creation():
    assert a.id == 4
    assert a.duration.to_secondes() == 0


def test_add_method(a: Album, c: Chanson):
    lst = [c]
    a.add(c)
    assert lst == a.titles
    long_song = Chanson("Long", "SnoopDog", Duree(50, 2, 23))
    a.add(long_song)
    assert lst == a.titles


test_album_creation()
test_add_method(a, c)

