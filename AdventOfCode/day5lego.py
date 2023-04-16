import sys

lines = [x for x in sys.stdin]

def go(reverse = False):
    st = [""]
    for line in lines:
        if line.startswith('['):
            for i, x in enumerate(line[1::4], start=1):
                while i >= len(st): st.append("")
                st[i] += x.strip()

        elif line.startswith('m'):
            n, a, b = map(int, line.split()[1::2])
            moved = st[a][:n]
            st[a] = st[a][n:]
            st[b] = (moved[::-1] if reverse else moved) + st[b]
    print(st)
    return ''.join(map(lambda x: x[0], filter(bool, st)))

print(go(True))
print(go())