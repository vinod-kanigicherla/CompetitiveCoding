import sys

grid = [list(line.strip()) for line in sys.stdin]
word = "MOJO"

def find_word(grid, word): #returns row and column positions of the characters of the word
	rows, cols = len(grid), len(grid[0])
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == word[0]:
				print(grid[i][j])
				positions = search_word(grid, word, i, j)
				if positions:
					return positions
	return None #what is returned when no word is found

def is_valid(r, c, lr, lc):
	return 0 <= r < lr and 0 <= c < lc

def search_word(grid, word, row, col):
	d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)] #displacement vectors
	print(word[0])
	for dr, dc in d:
		positions = [(row, col)]
		for char_i in range(1, len(word)):
			nr, nc = row + char_i*dr, col + char_i*dc
			if not is_valid(nr, nc, len(grid), len(grid[0])) or grid[nr][nc] != word[char_i]: break
			positions.append((nr, nc))
		if len(positions) == len(word):
			return positions
	return -1 #not found

def special_pattern(grid, word, row, col):
	r, c, i = row, col, 1
	pattern = [(0, 1), (1, 0), (0, 1)] #for example, square from mojo
	positions = [(row, col)]
	for dr, dc in pattern:
		nr, nc = r + dr, c + dc
		print(grid[nr][nc])
		print(nr, nc)
		if not is_valid(nr, nc, len(grid), len(grid[0])) or grid[nr][nc] != word[i]: break
		positions.append((nr, nc))
		i += 1
	if len(positions) == len(word):
		return positions
	return -1 #not found

print(find_word(grid, word))