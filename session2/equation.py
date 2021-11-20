# Trouver la solution d'équation de type x^a + y^b = z^c
# Guilherme Alvim Avila (4507-21-00) et Adrien Antonutti (3021-21-00)

# Renvoie le plus grand nombre d'une liste de nombre
def maximum(array):
    a = array[0]
    for i in array:
        if i > a:
            a = i
    return a

# Renvoie les diviseurs communs de 3 nombres quelconques


def diviseur_commun(a, b, c):
    diviseurs_commun = []
    # on part de 2 jusq'au plus grand nombre -1
    for i in range(2, maximum([a, b, c])):
        if a % i == 0 and b % i == 0 and c % i == 0:
            diviseurs_commun.append(i)
    return diviseurs_commun


# On demande les infos nécessaires :
a = int(input("Entrer la valeur de a : "))
b = int(input("Entrer la valeur de b : "))
c = int(input("Entrer la valeur de c : "))
max = int(input("Entrer la valeur max de x, y et z : "))
solutions = 0

# Permet de savoir si l'on doit afficher les racines ayant un divisuer commun
pas_de_diviseur_commun = False

# On parcour toutes les valeurs de x, y et z possible
for x in range(1, max):
    for y in range(1, max):
        for z in range(1, max):
            if (x**a + y**b) == z**c:
                # Vérification des diviseurs communs
                if not diviseur_commun(x, y, z) and pas_de_diviseur_commun == True:
                    print("Solutions trouvées : x=", x, " y =", y, " z=", z)
                    solutions += 1
                elif pas_de_diviseur_commun == False:  # Dans le cas où on affiche toutes les solutions
                    print("Solutions trouvées : x=", x, " y =", y, " z=", z)
                    solutions += 1
                else:
                    pass

# Affichage du nombre de solutions
if solutions == 0:
    print("Pas de solutions trouvées")
else:
    print(solutions, " solutions trouvées")
