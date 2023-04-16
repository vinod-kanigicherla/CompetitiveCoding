import sys
import numpy as np

temp = [line.strip().split() for line in sys.stdin]

print(temp)

X = 1
cycles = []
signal_strength = 0

for line in temp:
    if line[0] == 'noop':
        # (x, y) where x is # of cycles and y is value added
        cycles.append((1, 0))
    if line[0] == 'addx':
        V = int(line[1])
        cycles.append((2, V))

print(cycles)
stack = []

for (wait, value) in cycles:
    for _ in range(wait - 1):
        stack.append(0)
    stack.append(value)

print(stack)


positions = [20, 60, 100, 140, 180, 220]
print("stack len is ", len(stack))
for (i, position) in enumerate(positions):
    signal_strength += ((X + sum(stack[:position-1])) * position)

print(signal_strength)

cycle_values = [1]
for num in stack:
    cycle_values.append(cycle_values[-1] + num)

print(cycle_values)

sprite = "###....................................."
pixels = ['.']*240

# for (pixel_pos, pixel) in enumerate(pixels):
#     sprite_pos = sprite.index("###")
#     sprite_pos += stack[pixel_pos]
#
#     sprite = sprite.replace("###", "")
#     sprite = sprite[:sprite_pos] + "###" + sprite[sprite_pos:]
#
#     print(sprite + "\n")
#     print(stack[pixel_pos])
#     print(sprite_pos)

    # pixels[pixel_pos] = sprite[sprite_pos]


# start = 0
# end = 40
# line = "".join(pixels)
# for n in range(6):
#     print(line[start:end])
#     start += 40
#     end += 40

output = ""
for sprite_pos, value in enumerate(cycle_values):
    if cycle_values[sprite_pos] in range((sprite_pos % 40) - 1, (sprite_pos % 40) + 2):
        output += "#"
    else:
        output += "."

    if sprite_pos % 40 == 0:
        output += "\n"

print(output)

REHPRLUB