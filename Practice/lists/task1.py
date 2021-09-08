# │ ─ ┌ ┐ └ ┘
def make_table(rows):
    b = "┌─────────────────┐"
    t = b
    t += '\n'
    txt = '│ {:15} │'
    for x in rows:
        t += txt.format(x[0])
        t += '\n'
    c = "└─────────────────┘"
    t += c
    return t


table = make_table(
    rows=[
        ["Lemon"],
        ["Sebastiaan"],
        ["KutieKatj9"],
        ["Jake"],
        ["NotJoe"]
    ]
)
print(table)
