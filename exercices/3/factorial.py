def fact(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
