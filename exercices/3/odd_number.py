import math


def chiffres_pairs(n):
    if n > 0:
        digits = int(math.log10(n) + 1)
        return digits % 2 == 0
    else:
        return False
