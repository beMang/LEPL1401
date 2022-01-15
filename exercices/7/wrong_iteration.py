matrix = [
    [8, 11, 4],
    [7, 12, 9],
    [0, -6, 0],
]

sum_even = 0
i=0
l1 = len(matrix)
l2 = len(matrix[0])
while i<l1:
    j = 0
    while j<l2:
        elem = matrix[i][j]
        if elem % 2 == 0:
            sum_even += matrix[i][j]
        j+=1
    i+=1

# Normalement il faut utiliser des itérateurs, mais j'avais la flemme