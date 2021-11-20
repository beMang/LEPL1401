"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

from mission9 import *

"""
Test initial pour la classe Article.
@author Kim Mens
@version 4 novembre 2021
"""
articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49)
             ]

def test_articles(a_list) :
    for art in a_list :
        print(art)

"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles)

def test_facture(f) :
    print(f)

"""
Faire exécuter les différents tests.
"""

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)
    
def test_articlesreparation():
    article=ArticleReparation(0.75)
    assert article.prix()==46.25
    assert article.description()=="Réparation (0.75 heures)"
    article2=ArticleReparation(5)
    assert article2.prix()==195
    assert article2.description()=="Réparation (5 heures)"
    
def test_piece():
    piece1=Piece("souris bluetooth",15.99)   #test pour les différentes possibilitées de __eq__
    piece2=Piece("souris bluetooth",15.99)
    piece3=Piece("souris bluetooth",14)
    piece4=Piece("casque bluetooth",15.99)
    piece5=Piece("souris bluetooth",15.99, 1.5,True,True)
    assert piece1.__eq__(piece2)==True
    assert piece1.__eq__(piece3)==False
    assert piece1.__eq__(piece4)==False
    assert piece1.__eq__(piece5)==True
    assert piece1.description()=="souris bluetooth @ 15.99"
    assert piece2.description()=="souris bluetooth @ 15.99"
    assert piece1.prix()==15.99
    assert piece3.prix()==14
    assert piece1.poids()==0
    assert piece5.poids()==1.5
    assert piece2.fragile()==False
    assert piece5.fragile()==True
    assert piece5.tva_reduit()==True
    assert piece4.tva_reduit()==False

def test_articlepiece():
    piece1=Piece("souris bluetooth",15.99,0.6,False,True)
    piece2=Piece("Java in a Nutshell",24.00)
    article1=ArticlePiece(3,piece1)
    article2=ArticlePiece(2,piece2)
    print(article1.description())
    assert article1.description()=="3 * souris bluetooth @ 15.99"
    assert article2.description()=="2 * Java in a Nutshell @ 24.0"
    assert article1.prix()==47.97
    assert article2.prix()==48.00
    assert article1.taux_tva()==0.06
    assert article2.taux_tva()==0.21
    
def test_methode_livraison():
    article1=Piece("disque dur 350 GB",26, 0.355,True,True)
    piece1=Piece("souris bluetooth", 15.99, 0.176,True,True)
    article2=ArticlePiece(3,piece1)
    liste=[article1,article2]
    facture=Facture("PC Store - 22 novembre",liste)
    print(facture.print_livraison())

print("\n*** AUTRES TESTS ***\n")
test_articlesreparation()
test_piece()
test_articlepiece()
test_methode_livraison()
