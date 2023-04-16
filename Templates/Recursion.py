n = int(input()) #size of your grid
grid = [['.'] * n for _ in range(n)] #the empty grid that will be filled and returned
constraint = [list(input().strip()) for _ in range(n)] #the grid given
possibilities = [1, 2, 3, 4]
d = [(0, -1),(-1, 0), (1, 0), (0, -1)]
ids = [[None] * n for _ in range(n)] #required for other constraints (unique pieces, ids tatami)

def go(row, col):
    if row == n: return True #end
    if col == n: return go(row + 1, 0) #next row
    #if filled current row and col move to the next one
    if grid[row][col] != '.': return go(row, col+1) #fill

    #constraint to exit failed recursion here:for example:
    # if not corner_constraint(row, col):
    # 	return False

    #placing possibilities tatamis for example:
    #check horiz
    for possibility in possibilities:
        if check(row, col, possibility, 1, 0):
            put_tile(row, col, possibility, 1, 0)
            if go(row, col+1): return True
            remove_tile(row, col, possibility, 1, 0)

    #check vert
    for possibility in possibilities[1:]:
        if check(row, col, possibility, 0, 1):
            put_tile(row, col, possibility, 0, 1)
            if go(row, col+1): return True
            remove_tile(row, col, possibility, 0, 1)

    #no good states
    return False

def corner_constraint(r, c):
    row, col = r, c
    if row == 0 or col == 0: #not 3 adjacent tiles
        return True
    if ids[row-1][col] != ids[row][col-1] and ids[row][col-1] != ids[row-1][col-1] and ids[row-1][col-1] != ids[row-1][col]:
        return False
    return True

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def put_tile(r, c, num, dx, dy):
    row, col = r, c
    for _ in range(num):
        grid[row][col] = str(num)
        ids[row][col] = (r, c)
        row += dy
        col += dx

def remove_tile(r, c, num, dx, dy):
    row, col = r, c
    for _ in range(num):
        grid[row][col] = '.'
        ids[row][col] = None
        row += dy
        col += dx


def check(r, c, possibility, dx, dy):
    row, col = r, c
    for _ in range(possibility):
        if not is_valid(row, col): return False
        if grid[row][col] != '.': return False
        #if there is a constraint that doesn't match the possibility
        if constraint[row][col] != '.' and constraint[row][col] != str(possibility): return False
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if is_valid(row + dr, col + dc) and grid[row + dr][col + dc] == str(possibility): return False
        row += dy
        col += dx
    return True

go(0, 0)
for line in grid:
    print("".join(line))



