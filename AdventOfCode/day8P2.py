import sys

temp = [list(map(int, x.strip())) for x in sys.stdin]

def check_visible(row, col):
    curr = temp[row][col]

    up = []
    for above in temp[:row]:
        up.append(above[col])

    down = []
    for below in temp[row+1:]:
        down.append(below[col])

    left = temp[row][:col]
    right = temp[row][col+1:]

    #check up
    check_up = True
    for tree in reversed(up):
        if tree >= curr:
            check_up = False

    check_down = True
    for tree in down:
        if tree >= curr:
            check_down = False

    check_right = True
    for tree in right:
        if tree >= curr:
            check_right = False

    check_left = True
    for tree in reversed(left):
        if tree >= curr:
            check_left = False

    return check_up or check_left or check_right or check_down

def scenic_score(row, col):
    curr = temp[row][col]

    up = []
    for above in temp[:row]:
        up.append(above[col])

    down = []
    for below in temp[row + 1:]:
        down.append(below[col])

    left = temp[row][:col]
    right = temp[row][col + 1:]

    count_up = 0
    for tree in reversed(up):
        if tree < curr:
            count_up += 1
        elif tree >= curr:
            count_up += 1
            break

    count_down = 0
    for tree in down:
        if tree < curr:
            count_down += 1
        elif tree >= curr:
            count_down += 1
            break

    count_right = 0
    for tree in right:
        if tree < curr:
            count_right += 1
        elif tree >= curr:
            count_right += 1
            break

    count_left = 0
    for tree in reversed(left):
        if tree < curr:
            count_left += 1
        elif tree >= curr:
            count_left += 1
            break

    print(count_left, count_right, count_up, count_down, curr)
    return count_left * count_right * count_up * count_down

max_scenic_score = 0
for row in range(len(temp)):
    for col in range(len(temp[row])):
        max_scenic_score = max(max_scenic_score, scenic_score(row, col))

print(max_scenic_score)
