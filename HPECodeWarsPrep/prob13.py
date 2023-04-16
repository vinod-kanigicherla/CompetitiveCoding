import sys
lines = [line.strip() for line in sys.stdin]
width, height = [int(i) for i in lines[0].split(" ")]
grid = [["#" for j in range(width)] for i in range(height)]

for line in lines[1:]:
    if line.rstrip() == "END": break
    row, nums = line.split(":")
    spaces = [str(i) for i in nums.strip().split(" ")]
    for s in spaces:
        if s.find("-") != -1:
            start, end = [int(i) for i in s.strip().split("-")]
            for x in range(start, end+1):
                spaces.append(str(x))
        else:
            grid[int(row)][int(s)] = " "

for row in grid:
    s = ""
    for i in row:
        s += i
    print(s)