if b == 0:
    rest = None
else:
    while a > b:
        a -= b
    rest = a
