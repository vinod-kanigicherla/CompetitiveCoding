import sys
lines = [line.strip().split(" ") for line in sys.stdin]

scores = dict()
for line in lines:
    player_scores = list(map(int, line[:-1]))
    n1, n2, n3, n4, n5, n6 = player_scores
    n12 = (n1 - n2)
    n34 = (n3 - n4)
    n56 = (n5 - n6)
    if n12 < 0: n12 = 0
    if n34 < 0: n34 = 0
    if n56 < 0: n56 = 0
    scores[line[-1]] = n12 + n34 + n56


sorted_scores = sorted(scores.items(), key=lambda x:x[1])[::-1]
for k, v in sorted_scores:
    print(f"{k} {v}")

