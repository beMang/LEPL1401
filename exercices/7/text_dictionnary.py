def create_dictionary(filename):
    with open(filename, "r") as f:
        d = {}
        for line in f.readlines():
            words = line.split()
            for w in words:
                if d.get(w):
                    d[w] += 1
                else:
                    d[w] = 1
        return d

def occ(dictionnary, word):
    if dictionnary.get(word):
        return dictionnary.get(word)
    else:
        return 0