def rainfall(l):
    """
    pre: l est une liste de nombres, len(l) > 0, l contient un élément 9999.
    post: retourne la moyenne des éléments dans la liste l jusqu'à l'élément 9999
        non compris.  Si des éléments sont négatifs, ils sont traités comme valant 0.
    """
    if len(l) > 0:
        somme = 0
        i = 0
        for value in l:
            if value == 9999:
                break
            elif value > 0:
                somme += value
            else:
                pass
            i += 1
        return somme/i
    else:
        pass


# TESTS
assert rainfall([100, 50, 50, 250, 200, 9999]) == 130
assert rainfall([3, 5, -2, 4, 9999, 10]) == 3
