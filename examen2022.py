def n_facteur(n):
    if n==1:
        return 0
    else:
        number = n
        facteurs = []
        for i in range(2, n+1):
            count = 0
            while number%i == 0:
                count +=1
                number = number//i
            for j in range(count):
                facteurs.append(i)
        return(len(facteurs))
