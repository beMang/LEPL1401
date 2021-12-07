import math
# Ce fichier contient diverses fonctions qui ont été demandées lors du cours

def median(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            median = b
        else:
            median = c
    elif b >= c and b >= a:
        if a >= c:
            median = a
        else:
            median = c
    else:
        if a >= b:
            median = a
        else:
            median = b
    return median


def table_123():
    i = 1
    while i <= 10:
        print(i, "\t", (i*123))
        i += 1


def somme_entier(n):
    somme = 0
    i = 1
    while i <= n:
        somme += i
        i += 1
    return somme


def diviseurs(dividende):
    diviseurs = []
    i = 1
    while i <= dividende:
        if dividende % i == 0:
            diviseurs.append(i)
        i += 1
    return diviseurs


def rainfall(l):
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


def chiffres_pairs(n):
    if n > 0:
        digits = int(math.log10(n) + 1)
        return digits % 2 == 0
    else:
        return False


def matrice_carre(n):
    matrice = []
    for row in range(0, n):
        final_row = []
        for column in range(0, n):
            final_row.append(row*n + column)
        matrice.append(final_row)
    return matrice


def maximum_index(lst):
    max_value = 0
    max_index = 0
    current_index = 0
    for i in lst:
        if i > max_value:
            max_value = i
            max_index = current_index
        current_index += 1
    return max_index


def prime(max):
    if max <= 1:
        return []
    else:
        primes_number = [2]
        for i in range(3, max+1):
            is_prime = True
            for div in primes_number:
                if i % div == 0:
                    is_prime = False
                    break
            if is_prime == True:
                primes_number.append(i)
        return primes_number


def diff_count(lst):
    if not lst:
        return None
    else:
        diff = []
        for i in lst:
            try:
                diff.index(i)
            except ValueError:
                diff.append(i)
        return len(diff)


def croix(carac, n):
    if n % 2 != 0:
        for i in range(n):
            if n/2+0.5 == i+1:
                ligne = ""
                for i in range(n):
                    ligne += carac
                print(ligne)
            else:
                ligne = ""
                for i in range(n):
                    if n/2+0.5 == i+1:
                        ligne += carac
                    else:
                        ligne += " "
                print(ligne)


def maximum_index(lst):
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index


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


def carre():
    i = 1
    somme = 0
    while i <= 10:
        carre = i*i
        formule = i*(i+1)*(2*i+1)/6
        somme += carre
        print(i, "\t", carre, "\t", somme, "\t", int(formule))
        i += 1


def factorial(n):
    result = 1

    if n == 0:
        result = 1
    else:
        i = 1
        while i <= n:
            result *= i
            i += 1


def syracuse():
    s0 = input("Premier terme de la suite de syracuse")

    if(s0.isnumeric()):
        s0 = int(s0)
        print(s0)
        while s0 != 1:
            if s0 % 2 == 0:
                s0 = int(s0/2)
                print(s0)
            else:
                s0 = int(3*s0+1)
                print(s0)
    else:
        print("Entrée invalide, entier requis")
