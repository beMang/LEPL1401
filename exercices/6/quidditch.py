def referee(score_file):
    with open(score_file, "r") as f:
        lines = f.readlines()
        result = {}
        for i in range(len(lines)):
            if i == 0 or i==1:
                result[lines[i].strip()] = 0
            else:
                info = lines[i].split(" ", 1)
                if info[1].strip() == "vif d'or":
                    return info[0].strip()
                result[info[0]] += int(info[1])
        win = None
        for k, v in result.items():
            if not win:
                win = (k,v)
            else:
                if v > win[1]:
                    win = (k, v)
        return win[0]
