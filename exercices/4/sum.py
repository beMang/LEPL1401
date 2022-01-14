def sum(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += i
        elif type(i) == str:
            if i.isnumeric():
                sum += 1
        else:
            pass
    return sum
