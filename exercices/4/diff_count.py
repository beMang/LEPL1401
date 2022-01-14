def diff_count(lst):
    if not lst:
        return None

    else:
        diff = []
        for i in lst:
            try:
                diff.index(i)
            except ValueError:
                diff.append(i)
        return len(diff)
