import sys
import math

lines = [line.rstrip() for line in sys.stdin]
n, form, materials = lines[0], [int(i) for i in lines[1].split(" ")], [int(i) for i in lines[2].split(" ")]

ratios = []

for i in range(len(form)):
    ratios.append(math.ceil(materials[i] / form[i]))

bridges = sorted(ratios)[-1]
s = ""

for i in range(len(form)):
    needed = form[i] * bridges - materials[i]
    s += str(needed) + " "

print(s.rstrip())