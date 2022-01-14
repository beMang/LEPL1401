def line_count(filename):
    f = open(filename, "r")
    n = len(f.readlines())
    f.close()
    return n


def char_count(filename):
    f = open(filename, "r")
    count = 0
    for line in f:
        count += len(line)
    f.close()
    return count


def space(filename, n):
    f = open(filename, "w")
    f.write(n*" ")
    f.close()
    return True


def capitalize(filein, fileout):
    file = open(filein, "r")
    content = file.read().upper()
    file.close()
    file = open(fileout, "w")
    file.write(content)
    file.close()
    return True
