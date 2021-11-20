def capitalize(filein, fileout):
    file = open(filein, "r")
    content = file.read().upper()
    file.close()
    file = open(fileout, "w")
    file.write(content)
    file.close()
    return True

def space(filename, n):
    f = open(filename, "w")
    for i in range(n):
        f.write(" ")
    f.close()
    return True


def line_count(filename):
    f = open(filename, "r")
    n = len(f.readlines())
    f.close()
    return n
