import sys

temp = [list(map(int, x.strip())) for x in sys.stdin]

print(temp)

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

    print(right)

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

visible = 0


for row in range(len(temp)):
    for col in range(len(temp[row])):
        print(temp[row][col])
        if row == 0 or col == 0 or row == len(temp) - 1 or col == len(temp[row]) - 1:
            visible += 1
            continue

        if check_visible(row, col):
             visible += 1

print(visible)

