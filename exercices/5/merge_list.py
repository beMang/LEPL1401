def merge(first_list, second_list):
    result = []
    for e in first_list:
        result.append(e)
    for e in second_list:
        result.append(e)
    return sorted(result, key=lambda t: t[1])


lst1 = [['Charles', 44], ['Siegfried', 64], ['Kim', 77]]
lst2 = [['Olivier', 45], ['Peter', 55], ['Yves', 66]]

print(merge(lst1, lst2))