s = input()
pairs = 0
stack = []
for p in s:
    if p == "(":
        stack.append(p)
    elif p == ")":
        if len(stack) > 0:
            stack.pop()
            pairs += 1
print(pairs)