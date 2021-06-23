"""import textwrap


def text_wrap(s, w):
    wrapper = textwrap.TextWrapper(width=w)
    w_list = wrapper.wrap(s)
    return w_list

print(text_wrap("abdcuygbihkjhuh", 4))"""

n = int(input("enter"))
s = set(map(int, input("enter").split()))
N = int(input("enter"))
for i in range(0, N):
    command = input("enter").split(" ")

    e = int(command[1])
    if command[0] == "remove":
        if e in s:
            s.remove(e)
    elif command[0] == "discard":
        s.discard(e)
    elif command[0] == "pop":
        s.pop()
print(s)