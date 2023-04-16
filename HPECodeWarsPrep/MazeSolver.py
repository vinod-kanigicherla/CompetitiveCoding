from collections import deque

num_cols, num_rows = map(int, input().split(" "))

grid = [list(input()) for _ in range(num_rows)]

start_x, start_y = 0, 0
end_x, end_y = 0, 0

start_id = '@'
end_id = 'X'
obstacles = ['.', '\\', '/']

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
	delta_row = [-1, 0, 1, 0, 1, 1, -1, -1]
	delta_col = [0, 1, 0, -1, 1, -1, 1, -1]
	res = []
	for i in range(len(delta_row)):
		neighbor_row = row + delta_row[i]
		neighbor_col = col + delta_col[i]
		if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols and grid[neighbor_row][
			neighbor_col] not in obstacles:
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
			print(visited_steps[(node.x, node.y)])
			get_path(node, path)
			return path
		for neighbor in get_neighbors(node):
			if (neighbor.x, neighbor.y) in visited_steps:
				continue
			queue.append(neighbor)
			visited_steps[(neighbor.x, neighbor.y)] = visited_steps[(node.x, node.y)] + 1


path = bfs(Node(start_x, start_y))
print(path)

# Marking Path
mark = "*"

for node in path:
	row, col = node.x, node.y
	grid[row][col] = mark

# Printing Grid
for row in grid:
	print("".join(row))
