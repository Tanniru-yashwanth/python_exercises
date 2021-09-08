# │ ─ ┌ ┐ └ ┘
def make_table(rows):
    maxi = 0
    for i in rows:
        if len(i[0]) > maxi:
            maxi = len(i[0])
    print(maxi)
    maxi += 2
    b = "┌" + maxi * "─" + "┐"
    t = b
    t += '\n'
    txt = '│ {:10} │'
    for x in rows:
        t += txt.format(x[0])
        t += '\n'
    c = "└" + maxi * "─" + "┘"
    t += c
    return t


table = make_table(
    rows=[
        ["Lemon"],
        ["Sebastiaan"],
        ["KutieKatj9"],
        ["Jake"],
        ["Not Joe"]
    ]
)
print(table)
