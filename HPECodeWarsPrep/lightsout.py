import sys
q = [] #on_list
grid = []
visited = dict() #visited with steps
idx = 0
steps = 0
# #-on .-off

board = [list(line.strip()) for line in sys.stdin]

disp = [(0,0), (0, 1), (0, -1), (1, 0), (-1, 0)]
adj = []

def update(grid, curr):
    next_grid = grid.copy()
    curr_r, curr_c = curr
    neighbors = [(curr_r + dr, curr_c + dc) for dr, dc in disp if 0 <= curr_r + dr <= 4 and 0 <= curr_c + dc <= 4]

    for button in neighbors:
        if button in grid:
            next_grid.remove(button)
        else:
            next_grid.append(button)
    return next_grid


for row in range(len(board)):
    for col in range(len(board[row])):
        adj.append((row, col))
        if board[row][col] == '#':
            grid.append((row, col))

if len(grid) == 0:
    print(0)

q.append(grid)
visited[tuple(grid)] = idx

print(visited)

while idx < len(q):
    curr_grid = q[idx].copy()
    if len(curr_grid) == 0:
        print("FINAL IDX: ",idx)
        break
    else:
        for click in adj:
            new_grid = update(curr_grid, click)
            if tuple(new_grid) not in visited:
                q.append(new_grid)
                print(q)
                visited[tuple(new_grid)] = visited[tuple(curr_grid)] + 1
        idx += 1
