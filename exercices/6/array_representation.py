def header(width) -> str:
    s = "+"
    s += (width+2)*"-"
    s += "+\n"
    return s


def line(l, width):
    l = l.strip()
    s = ("| {:<" + str(width) + "} |\n").format(l[0:width])
    return s


def table(filename_in, file_name_out, width):
    s = header(width)
    with open(filename_in, "r") as f:
        for l in f.readlines():
            s += line(l, width)
    s += header(width)
    with open(file_name_out, "w+") as f:
        f.write(s.strip())
