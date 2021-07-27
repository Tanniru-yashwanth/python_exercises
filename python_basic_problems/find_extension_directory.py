# Python Program to Find All File with .txt Extension Present Inside a Directory
import os

a = os.listdir("S:/material")
for x in a:
    if x.endswith(".txt"):
        print(x)