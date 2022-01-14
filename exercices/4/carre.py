def carre(n):
    matrice = []
    for row in range(0, n):
        final_row = []
        for column in range(0, n):
            final_row.append(row*n + column)
        matrice.append(final_row)
    return matrice
