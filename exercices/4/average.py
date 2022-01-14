def average(list):
    if not list:
        return None
    else:
        sum = 0
        for i in list:
            sum += i
        return sum/len(list)
