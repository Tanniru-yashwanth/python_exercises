
def solve(s):
    t = s.isalpha()
    if t is True:
        a = s.split(" ")
        c = [x.title() for x in a]
        print(" ".join(c))
    else:
        print(s)


solve("tanniru yashwanth")
