from collections import deque

num_rows, num_cols = map(int, input().split(" "))

grid = [input().split(" ") for _ in range(num_rows)]

start_x, start_y = 0, 0
end_x, end_y = 0, 0

start_id = 'S'
end_id = 'X'

# x is row and y is col!
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == start_id:
            start_x, start_y = i, j
        if grid[i][j] == end_id:
            end_x, end_y = i, j


# check start x and y: print(start_x, start_y, end_x, end_y)
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return str((self.x, self.y))


def get_path(node, path):
    if node:
        get_path(node.parent, path)
        path.append(node)


def get_neighbors(curr):
    row, col = curr.x, curr.y
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            if grid[row][col] == 'S':
                res.append(Node(neighbor_row, neighbor_col, curr))
            elif grid[neighbor_row][neighbor_col] == 'X':
                res.append(Node(neighbor_row, neighbor_col, curr))
            elif grid[neighbor_row][neighbor_col] != 'S':
                if int(grid[neighbor_row][neighbor_col]) <= int(grid[row][col]) and 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    res.append(Node(neighbor_row, neighbor_col, curr))

    return res


def bfs(starting_node):
    queue = deque()
    idx = 0
    visited_steps = {(starting_node.x, starting_node.y): idx}
    queue.append(starting_node)

    while len(queue) > 0:
        node = queue.popleft()
        idx += 1
        if node.x == end_x and node.y == end_y:
            path = []
            # steps:
            get_path(node, path)
            return path
        for neighbor in get_neighbors(node):
            if (neighbor.x, neighbor.y) in visited_steps:
                continue
            queue.append(neighbor)
            visited_steps[(neighbor.x, neighbor.y)] = visited_steps[(node.x, node.y)] + 1


path = bfs(Node(start_x, start_y))

# Marking Path
mark = "."

for node in path[1:-1]:
    row, col = node.x, node.y
    grid[row][col] = mark

unvisited_mark = "#"
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] not in ['S', 'X', '.']:
            grid[i][j] = '#'

# Printing Grid
for row in grid:
    print(" ".join(row))
