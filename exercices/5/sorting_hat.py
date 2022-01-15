knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

def house_designation(student_qualities):
    info = []
    for house in knowledge:
        count = 0
        for quality in house[1]:
            if quality in student_qualities:
                count += 1
        info.append((house[0], count))
    print(info)

    info = sorted(info, key=lambda t:t[1], reverse=True)
    print(info)
    result = []

    for i in info:
        result.append(i[0])

    return result
