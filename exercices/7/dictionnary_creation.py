def create_index(lists_of_words):
    index = {}
    for i in range(len(lists_of_words)):
        if index.get(lists_of_words[i]) == None:
            index[lists_of_words[i]] = [i]
        else:
            index[lists_of_words[i]].append(i)
    return index


def create_dict(l):
    d = {}
    for x, y in l:
        if not d.get(x):
            d[x] = [y]
        else:
            d[x].append(y)
    return d


def create_dict_max(l):
    d = {}
    for x, y in l:
        if not d.get(x):
            d[x] = y
        else:
            if y>d[x]:
                d[x] = y
    return d
