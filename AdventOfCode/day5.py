import sys
temp = [line for line in sys.stdin]

stacks = {i:[] for i in range(1, 10)}

for line in temp:
    if '[' not in line:
        break
    for stack_num, i in enumerate(range(1, len(line), 4)):
        if line[i] != ' ':
            stacks[stack_num + 1].append(line[i])


for stack in stacks.values():
    stack.reverse()

movements = []

for line in temp[temp.index('\n') + 1:]:
    l = line.replace("move ", "").replace(" from ", " ").replace(" to ", " ")
    vals = l.split(" ")
    movements.append((vals[0], vals[1], vals[2]))


for num_items, origin, dest in movements:
    moved = []
    for i in range(int(num_items)):
        moved.append(stacks[int(origin)].pop())
    for to_move in reversed(moved):
        stacks[int(dest)].append(to_move)


result = "".join(stacks[s][-1] for s in range(1, len(stacks.values()) + 1) if stacks[s])
print(result)