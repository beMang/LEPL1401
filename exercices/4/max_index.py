def maximum_index(lst):
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index
