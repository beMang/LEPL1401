def is_voyelle(carac):
    voyelle = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    for i in voyelle:
        if i == carac:
            return True
    return False

def is_majuscule(carac):
    if carac.lower() == carac:
        return False
    else:
        return True


def extract(code):
    result = ""
    for c in code:
        if is_voyelle(c):
            result+="vowel"
            if is_majuscule(c):
                result+=("-up ")
            else:
                result+=("-low ")
        elif c.isnumeric():
            result += "number "
        else:
            result += "consonant"
            if is_majuscule(c):
                result += ("-up ")
            else:
                result += ("-low ")
    return result.strip()

def treatment(data):
    data = data.split()
    current_count = 1
    result = ""
    for i in range(len(data)):
        if i == len(data)-1 :
            print("denier")
            if data[i] == data[i-1]:
                result += data[i] + "*" + (current_count).__str__() + " "
            else:
                result += data[i] + "*1 "
        elif data[i] == data[i+1]:
            current_count += 1
        else:
            result += data[i] + "*" + current_count.__str__() + " "
            current_count = 1

    return result.strip()
