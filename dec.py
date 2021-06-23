def wrapper(f):
    def fun(l):
        # complete the function
        for x in l:
            if len(x) == 10:
                x = "+91" + x[0:5] + " " + x[5:10]
            elif len(x) == 11:
                x = "+91" + x[1:6] + " " + x[6:11]
            elif len(x) == 12:
                x = "+91" + x[2:7] + " " + x[7:12]
            elif len(x) == 13:
                x = "+91" + x[3:8] + " " + x[8:13]
            return l
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


l = ["07895462130", "919875641230", "9195969878"]
sort_phone(l)
