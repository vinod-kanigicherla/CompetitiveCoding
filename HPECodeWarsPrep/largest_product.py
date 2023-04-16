import sys
from functools import reduce

grid = [list(map(int, line.strip().split(" "))) for line in sys.stdin]

r, c = 0, 0
max_prod = -float("inf")

#horizontal
for r in range(len(grid)):
    for c in range(len(grid[r]) - 3):
        max_prod = max(reduce(lambda x, y: x*y, grid[r][c: c+4]), max_prod)
#vertical
for r in range(len(grid) - 3):
    for c in range(len(grid[r])):
        max_prod = max(reduce(lambda x, y: x*y, [row[c] for row in grid[r: r+4]]), max_prod)

#diagonal left
for r in range(len(grid) - 3):
    for c in range(len(grid[r]) - 3):
        max_prod = max(grid[r][c] * grid[r+1][c+1] * grid[r+2][c+2] * grid[r+3][c+3], max_prod)

#diagonal right
for r in range(2, len(grid)):
    for c in range(len(grid[r]) - 3):
        max_prod = max(grid[r][c] * grid[r-1][c+1] * grid[r-2][c+2] * grid[r-3][c+3], max_prod)

print(max_prod)
