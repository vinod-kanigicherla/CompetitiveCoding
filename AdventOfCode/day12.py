import sys
import string
from collections import deque as queue


letters = string.ascii_letters
temp = [list(line.strip()) for line in sys.stdin]

direction_x = [ -1, 0, 1, 0]
direction_y = [ 0, 1, 0, -1]

rows = len(temp)
cols = len(temp[0])
visited = [[False]*cols]*rows

print(temp)


def isValid(visited, nrow, ncol, crow, ccol):
    #out-of-bounds
    if (nrow < 0 or ncol < 0 or nrow >= rows or ncol >= cols):
        return False
    #already-visited
    if (visited[nrow][ncol]):
        return False

    if temp[crow][ccol] == 'S':
        return True

    return True

def can_move(curr_letter, to_letter):
    print(curr_letter)
    print(to_letter)
    return letters.index(curr_letter) == letters.index(to_letter) - 1 or letters.index(curr_letter) == letters.index(to_letter)

steps = float("inf")

def BFS(temp, visited, row, col):
    q = queue()
    q.append((row, col))
    visited[row][col] = True

    while len(q) > 0:
        curr = q.popleft()
        curr_x, curr_y = curr
        print(temp[curr_x][curr_y])

        for direction_index in range(len(direction_x)): #adjacent elements
            next_x = curr_x + direction_x[direction_index]
            next_y = curr_y + direction_y[direction_index]

            if isValid(visited, next_x, next_y, curr_x, curr_y):
                q.append((next_x, next_y))
                print(temp[next_x][next_y])
                visited[next_x][next_y] = True


BFS(temp, visited, 0, 0)
print(visited)
