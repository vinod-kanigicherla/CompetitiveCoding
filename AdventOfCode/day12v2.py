import sys
from string import ascii_letters as letters

temp = [list(line.strip()) for line in sys.stdin]

visited = [] # queue
steps = dict() # matches position with number of steps
idx = 0
start, end = (), ()
moves = [(1, 0), (-1, 0), (0, 1), (0,-1)]

rows = len(temp)
cols = len(temp[0])
# returns a list of next possible moves
def next_moves(curr_x, curr_y):
    nmoves = list()
    for move_x, move_y in moves:
        next_x, next_y = curr_x + move_x, curr_y + move_y

        #out of bounds
        if not (next_x < 0 or next_y < 0 or next_y >= rows or next_x >= cols):
            print(temp[curr_y][curr_x])
            curr_i = letters.index(temp[curr_y][curr_x])
            next_i = letters.index(temp[next_y][next_x])

            if temp[curr_y][curr_x] == 'S' and temp[next_y][next_x] == 'a':
                nmoves.append((next_x, next_y))

            if next_i <= curr_i + 1:
                nmoves.append((next_x, next_y))

            #special end case
            if temp[curr_y][curr_x] == 'z' and temp[next_y][next_x] == 'E':
                nmoves.append((next_x, next_y))

    return nmoves

#Gives start and end positions
for row_index, row in enumerate(temp):
    for col_index, letter in enumerate(row):
        if letter == "S":
            start = (col_index, row_index)
            visited.append(start)
            steps[start] = idx
        if letter == "E":
            end = (col_index, row_index)


while idx < len(visited):
    curr_x, curr_y = visited[idx]
    idx += 1
    if (curr_x, curr_y) == end:
        print(steps[(curr_x, curr_y)])
        break
    for next_x, next_y in next_moves(curr_x, curr_y):
        visited.append((next_x, next_y))
        steps[(next_x, next_y)] = steps[(curr_x, curr_y)] + 1
