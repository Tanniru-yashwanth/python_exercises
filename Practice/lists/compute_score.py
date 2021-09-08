def compute_score(score_entries):
    lst = []
    for x in score_entries:
        if x == "+":
            lst.append(int(lst[-1]) + int(lst[-2]))
        elif x == "D":
            lst.append(int(lst[-1]) * 2)
        elif x == "C":
            lst.pop(-1)
        elif x.lstrip('-').isdigit():
            lst.append(int(x))

    s = sum(lst)
    return s





