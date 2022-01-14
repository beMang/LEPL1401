def equal(l, d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            try:
                if d[(i, j)] != l[i][j]:
                    return False
            except KeyError:
                if l[i][j] != 0:
                    return False
    return True
