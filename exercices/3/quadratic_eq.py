import math

def rho(a, b, c):
    return b**2 - 4*a*c


def n_solutions(a, b, c):
    if rho(a, b, c) > 0:
        return 2
    elif rho(a, b, c) == 0:
        return 1
    else:
        return 0


def solution(a, b, c):
    if n_solutions(a, b, c) > 1:
        if a > 0:
            return (-b - math.sqrt(rho(a, b, c)))/(2*a)
        else:
            return (-b + math.sqrt(rho(a, b, c)))/(2*a)
    elif n_solutions(a, b, c) == 1:
        return (-b+rho(a, b, c))/(2*a)
    else:
        return None
