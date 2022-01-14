def minimum(array):
    a = array[0]
    for i in array:
        if i < a:
            a = i
    return a


minima = minimum([a, b, c])
