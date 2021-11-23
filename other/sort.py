def sort(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(lst[i])
        else:
            for j in range(len(result)):
                if j==len(result)-1:
                    if result[j]>= lst[i]:
                        result.insert(j-1, lst[i])
                    else:
                        result.append(lst[i])
                else:
                    if result[j] <= lst[i] <= result[j+1]:
                        result.insert(j-1, lst[i])
                        break
    return result


print(sort([59, 37, 67, 44, 44, 93, 86, 100, 16, 96, 59, 26, 100, 47]))
