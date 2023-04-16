from collections import deque
from string import ascii_letters as letters

num_rows, num_cols = map(int, input().split(" "))

grid = [list(input()) for _ in range(num_rows)]

start_x, start_y = 0, 0
end_x, end_y = 0, 0

start_id = 'S'
end_id = 'X'
obstacles = ['#']
valves = []
possible_valves = list(letters[:10])
possible_fires = list(map(lambda letter: letter.upper(), letters[:10]))


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == start_id:
            start_x, start_y = i, j
        if grid[i][j] == end_id:
            end_x, end_y = i, j
        if grid[i][j] in possible_valves:
            valves.append((grid[i][j],i, j))

# check start x and y: print(start_x, start_y, end_x, end_y)
class Node:
    def __init__(self, x, y, valves, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.valves = valves

    def __repr__(self):
        return str((self.x, self.y))


def get_path(node, path):
    if node:
        get_path(node.parent, path)
        path.append(node)


def get_neighbors(curr):
    row, col, open_valves = curr.x, curr.y, list(curr.valves)

    for open_valve, valve_row, valve_col in open_valves:
        if grid[row][col] == open_valve:
            open_valves.remove((open_valve, valve_row, valve_col))


    delta_row = [-1, 0, 1, 0] # for diagonals: , 1, 1, -1, -1
    delta_col = [0, 1, 0, -1] # for diagonals: , 1, -1, 1, -1
    res = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if not (0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols): continue
        if grid[neighbor_row][neighbor_col] in obstacles: continue

        open_valves_letters = [open_valve for open_valve, valve_row, valve_col in open_valves]
        if grid[neighbor_row][neighbor_col] in possible_fires:
            if grid[neighbor_row][neighbor_col].lower() in open_valves_letters: continue

        res.append(Node(neighbor_row, neighbor_col, tuple(open_valves), curr))

    return res


def bfs(starting_node):
    queue = deque()
    idx = 0
    visited_steps = {(starting_node.x, starting_node.y, starting_node.valves): idx}
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
            if (neighbor.x, neighbor.y, neighbor.valves) in visited_steps:
                continue
            queue.append(neighbor)
            visited_steps[(neighbor.x, neighbor.y, neighbor.valves)] = visited_steps[(node.x, node.y, node.valves)] + 1


path = bfs(Node(start_x, start_y, tuple(valves)))

final = ""
for node in path:
    row, col = node.x, node.y
    if grid[row][col] == "S" or grid[row][col] in possible_valves or grid[row][col] in possible_fires:
        final = final + grid[row][col] + " "
    if grid[row][col] == "X":
        final = final + grid[row][col]

print(final)