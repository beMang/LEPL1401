from cmath import inf
from typing import Iterable


students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}

def winning_house(scroll):
    results = {}
    with open(scroll, "r") as f:
        for l in f.readlines():
            info = l.split()
            for k,v in students.items():
                if info[0] in students[k]:
                    if results.get(k):
                        results[k] += int(info[1])
                    else:
                        results[k] = int(info[1])
    win = None
    for k, v in results.items():
        if not win:
            win = k
        else:
            if type(win) == list:
                if results[win[0]] < v:
                    win = k
                elif results[win[0]] == v:
                    win.append(k)
                else:
                    pass
            else:
                if v>results[win]:
                    win = k
                elif v==results[win]:
                    win = [k, win]
                else:
                    pass
    if type(win) == list:
        win.reverse()
    return win

print(winning_house("test"))
