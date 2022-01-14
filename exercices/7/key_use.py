def get_country(l, name):
    for e in l:
        if e["City"] == name:
            return e["Country"]
    return False