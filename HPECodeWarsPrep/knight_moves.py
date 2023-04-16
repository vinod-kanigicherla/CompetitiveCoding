import sys

chess_board = [list(line.strip()) for line in sys.stdin]

obstacles = []
impossible = True

steps = [] #q
tracker = dict() #counts number of moves

moves = [(2, 1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (-2, -1)]
idx = 0

for y, row in enumerate(chess_board):
    for x, pos in enumerate(row):
        if pos == 'S':
            S = (x, y)
            steps.append((x,y))
            tracker[(x,y)] = idx
        elif pos == 'T':
            T = (x, y)
        elif pos == '#':
            obstacles.append((x,y))

def next_moves(curr_x, curr_y):
    next_list = []

    for next in moves:
        next_x, next_y = curr_x + next[0], curr_y + next[1]
        #inside board
        if not (next_x < 0 or next_y < 0 or next_y >= len(chess_board) or next_x >= len(chess_board[0]) or (next_x, next_y) in obstacles or (next_x, next_y) in steps):
            next_list.append((next_x, next_y))

    return next_list


while idx < len(steps):
    curr_x, curr_y = steps[idx]
    idx += 1

    if (curr_x, curr_y) == T:
        print(tracker[(curr_x, curr_y)])
        impossible = False
        break

    for next_x, next_y in next_moves(curr_x, curr_y):
        steps.append((next_x, next_y))
        tracker[(next_x, next_y)] = tracker[(curr_x, curr_y)] + 1


print(S, T, obstacles)

if impossible:
    print("-1")
