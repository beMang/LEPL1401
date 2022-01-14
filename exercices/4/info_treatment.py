def treatment(data):
    data = data.split()
    current_count = 1
    result = ""
    for i in range(len(data)):
        if i == len(data)-1:
            print("denier")
            if data[i] == data[i-1]:
                result += data[i] + "*" + (current_count).__str__() + " "
            else:
                result += data[i] + "*1 "
        elif data[i] == data[i+1]:
            current_count += 1
        else:
            result += data[i] + "*" + current_count.__str__() + " "
            current_count = 1

    return result.strip()
