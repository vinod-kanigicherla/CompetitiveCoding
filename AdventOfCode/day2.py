import sys
temp = [line.strip().split() for line in sys.stdin]
print(temp)

score = 0
key = {'X': 'A', 'Y': 'B', 'Z': 'C'}

for moves in temp:
    opponent_move = moves[0]
    my_move = moves[1]

    if my_move == 'X':
        if opponent_move == 'B':
            score += 1
        elif opponent_move == 'C':
            score += 2
        elif opponent_move == 'A':
            score += 3

    if my_move == 'Y':
        if opponent_move == 'A':
            score += 4
        elif opponent_move == 'B':
            score += 5
        elif opponent_move == 'C':
            score += 6

    if my_move == 'Z':
        if opponent_move == 'A':
            score += 8
        elif opponent_move == 'B':
            score += 9
        elif opponent_move == 'C':
            score += 7

print(score)