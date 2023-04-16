import sys

grid = [list(line.strip()) for line in sys.stdin]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = []
steps = dict()
idx = 0

#STARTING POSITION CODE HERE

while idx < len(q):
    #curr_state = (row, col) or grid
    idx += 1
    #END CONDITION CODE HERE
    # for (next row, next col) of neighbors or move in possible moves
    # if move or (next row, next col) in d: continue (visited check)
    #q.append((next row, next col))
    #d[(next row, next col)] = d[(curr row, curr col)] + 1