def mix(l):
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d’entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    r = []
    for i in range(0,int(len(l)/2)):
        r.append(l[i])
        r.append(l[len(l)-i-1])
    return r