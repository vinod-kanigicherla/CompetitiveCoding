import sys

grid = [list(line.strip()) for line in sys.stdin]
possibilities = ["#", "."] #for example

n = 4 #dimensions of your board

def fill(row, col):
    if row == n:
        for line in grid:
            print("".join(line))
        return True
    elif col == n:
        return fill(row+1, 0)

    for option in possibilities:
        grid[row][col] = option
        fill(row, col + 1)
    return False

fill(0, 0)