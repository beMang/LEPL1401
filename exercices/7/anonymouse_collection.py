def collect(file):
    with open(file, "r") as f:
        d = {}
        for l in f.readlines():
            pattern = treatment(extract(l))
            if d.get(pattern):
                d[pattern] +=1
            else:
                d[pattern] = 1
    return d

# ne passe pas dans inginious