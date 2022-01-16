def combien(n):    # Ne pas effacer cette ligne
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d’entiers consecutifs
           strictement positifs dont la somme est egale a n
    """
    result = 0
    for i in range(1, n+1):
        sum = 0
        j=i
        while sum<n:
            sum +=j
            j+=1
        if sum == n:
            result +=1
    return result
