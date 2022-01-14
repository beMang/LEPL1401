def diviseurs(dividende):
    diviseurs = []
    i = 1
    while i < dividende:
        if dividende % i == 0:
            diviseurs.append(i)
        i += 1
    return diviseurs


for i in range(1, n+1):
    print(i, ":", len(diviseurs(i)))
