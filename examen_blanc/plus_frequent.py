def plus_frequent(l):
    """
    pre: `l` est une liste, len(l) > 0
    post: retourne l'élément qui se trouve le plus grand nombre de fois
        dans la liste `l` (nombre d'ocurrences égales au sens de ==).  Si
        plusieurs éléments différents apparaissent un plus grand nombre égal
        de fois, retourne le premier apparaissant dans la liste.
    """
    if not l:
        return None
    else:
        d = {}
        for e in l:
            if not d.get(e):
                d[e] = 1
            else:
                d[e] += 1
        max = l[0]
        for k, v in d.items():
            if type(max) == list:
                if v > d[max[0]]:
                    max = k
                elif v == d[max[0]]:
                    max.append(k)
                else:
                    pass
            else:
                if v > d[max]:
                    max = k
                elif v == d[max]:
                    if max != k:
                        max = [max, k]
                else:
                    pass
        return max


# TESTS
assert plus_frequent([1, 2, 2, 2, 3, 4, 9, 9, 9]) == [2, 9]
assert plus_frequent([1, 2, 2]) == 2
assert plus_frequent([10]) == 10
assert plus_frequent([]) == None
