def recherche(m, v):
    for row in m:
        for number in row:
            if number == v:
                return True

    return False
