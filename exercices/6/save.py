def save_data(filename, life, mana, position_x, position_y):
    with open(filename, "w+") as f:
        s = ("{}\n"*4).format(life, mana, position_x, position_y)
        f.write(s.strip())


def load_data(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        t = (
            int(lines[0]),
            int(lines[1]),
            float(lines[2]),
            float(lines[3])
        )
        return t
