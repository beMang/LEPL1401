if a >= b and a >= c:
    if b >= c:
        median = b
    else:
        median = c
elif b >= c and b >= a:
    if a >= c:
        median = a
    else:
        median = c
else:
    if a >= b:
        median = a
    else:
        median = b