import sys

cakes = [list(line.strip()) for line in sys.stdin]
possibilities = ["v", "c"]
print(cakes)

n = 4

states = 0

def fill(row, col):
    global states
    if row == n:
        print(cakes)
        states += 1
        return True
    elif col == n:
        return fill(row+1, 0)

    for x in possibilities:
        cakes[row][col] = x
        fill(row, col + 1)
    return False

fill(0, 0)
print(states)