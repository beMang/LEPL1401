def triangle(n):
    tableau = []
    for i in range(0, n+1):
        tableau.append([])
        for j in range(0, i+1):
            tableau[i].append(j)
    return tableau