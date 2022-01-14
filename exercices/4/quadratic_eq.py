def solveur(lst):
    if not lst and len(lst) != 3:
        return []
    else:
        solutions = []
        for i in lst:
            solutions.append(solution(i[0], i[1], i[2]))

        return solutions
