def read_coordinate(filename):
    lst = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.split(",")
            lst.append((float(line[0]), float(line[1])))
    return lst

def write_coordinates(filename, l):
    s = ""
    for c in l:
        s += "{},{}\n".format(c[0], c[1])
    with open(filename, "w+") as f:
        f.write(s)
