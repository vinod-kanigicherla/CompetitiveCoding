import sys

temp = [line.strip().split() for line in sys.stdin]

visited = set()
visited.add((0,0))

move_set = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

prev_head_moves = [(0,0)]
prev_tail_moves = [(0,0)]


def move_ht(direction, moves):
    head_x, head_y = prev_head_moves[-1]
    tail_x, tail_y = prev_tail_moves[-1]

    for move in range(moves):
        move_x, move_y = move_set[direction]
        head_x += move_x
        head_y += move_y

        while abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
            if head_x > tail_x:
                tail_x += 1
            elif tail_x > head_x:
                tail_x -= 1

            if head_y > tail_y:
                tail_y += 1
            elif tail_y > head_y:
                tail_y -= 1

            visited.add((tail_x, tail_y))

        prev_head_moves.append((head_x, head_y))
        prev_tail_moves.append((tail_x, tail_y))


last_seen = set()
snake = [(0, 0)]*10
def move_big_ht(direction, moves):
    move_x, move_y = move_set[direction]
    for head in range(moves):
        head_x, head_y = snake[0]
        snake[0] = head_x + move_x, head_y + move_y

        for i in range(1, len(snake)):
            prev_x, prev_y = snake[i]
            curr_x, curr_y = snake[i - 1]
            # print("prev: ", (prev_x, prev_y))
            # print("curr: ", (curr_x, curr_y))

            while abs(prev_x - curr_x) > 1 or abs(prev_y - curr_y) > 1:
                if prev_x > curr_x:
                    prev_x -= 1
                elif curr_x > prev_x:
                    prev_x += 1

                if prev_y > curr_y:
                    prev_y -= 1
                elif curr_y > prev_y:
                    prev_y += 1

            snake[i] = (prev_x, prev_y)

        last_seen.add(snake[-1])


for [direction, moves] in temp:
    move_ht(direction, int(moves))
    move_big_ht(direction, int(moves))

print(len(visited))#Part1
print(len(last_seen))#Part2