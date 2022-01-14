def ajoute(l, v):
    find = False
    for value in l:
        if value == v:
            find = True
            break
    if find == False:
        l.append(v)
