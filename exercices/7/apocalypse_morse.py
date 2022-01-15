from unittest.loader import VALID_MODULE_NAME


def translate(data):
    for c in data:
        if morse.get(c):
            data = data.replace(c, morse[c])
        else:
            raise ValueError("Caractère non connu en morse")
    return data


def translate(data:str, lan):
    s=""
    for w in data.split():
        if lan.get(w.lower().strip()):
            s += lan[w.lower().strip()] + " "
        else:
            s+= w + " "
    return s.strip()
