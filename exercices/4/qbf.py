def positions(p:str, s:str):
    s = s.lower()
    p = p.lower()
    position = []
    for i in range(len(s) - len(p) + 1):
        valid = True
        for j in range(len(p)):
            if p[j] == "?":
                pass
            else:
                if p[j] != s[i+j]:
                    valid = False
        if valid:
            position.append(i)
    return position


print(positions("ab", "CDEF"))
print(positions("?B", "CAbDEF"))
print(positions("A?", "CABDEACF"))
print(positions("aa", "CAAABDEAAF"))
print(positions("??", "CAAAB"))
