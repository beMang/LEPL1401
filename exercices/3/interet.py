def interests(base, y, x):
    for i in range(0, x):
        base *= (1+y/100)
    return base
