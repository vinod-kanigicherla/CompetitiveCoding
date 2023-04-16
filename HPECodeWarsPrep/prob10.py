p = input()
lefts = p.count("(")
rights = p.count(")")
pairs = 0

while p != "":
    l_i = p.find("(")
    if l_i != -1:
        r_i = p[l_i:].find(")")
        if r_i != -1:
            p_list = list(p)
            p_list.pop(l_i)
            p_list.pop(r_i-1)
            pairs += 1
            p = "".join(p_list)


"""while len(p) > 0:
    li = p.index("(")
    i = li
    while i < len(p):
        if p[i] == ")":
            p.pop(li)
            p.pop(i)
            pairs += 1
            i -= 1
            break
        else:
            i += 1
    if all(c == p[0] for c in p):
        break"""

print(f"Total left: {lefts}")
print(f"Total right: {rights}")
print(f"Total pairs: {pairs}")
if lefts == rights == pairs:
    print("Balanced")
else:
    print("Unbalanced")
