f, r, g, b = map(int, input().split())


def combinations(level, f, r, g, b, prev=None):
    if level == 4: return 1 if f == 0 else 0
    res = combinations(level + 1, f, r, g, b)
    if r > 0 and prev != 'r': res += combinations(level + 1, f - 1, r - 1, g, b, 'r')
    if b > 0 and prev != 'b': res += combinations(level + 1, f - 1, r, g, b - 1, 'b')
    if g > 0 and prev != 'g': res += combinations(level + 1, f - 1, r, g - 1, b, 'g')
    return res


print(combinations(0, f, r, g, b))

