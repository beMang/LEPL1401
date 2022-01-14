def write(letter_template, name):
    s = ""
    with open(letter_template, "r") as f:
        for line in f.readlines():
            s += line.replace("#", name)
    with open(letter_template, "w") as f:
        f.write(s)
