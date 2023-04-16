import sys
temp = [line.strip().split(",") for line in sys.stdin]

pair = 0
for assign in temp:
    first_elf = set(range(int(assign[0].split("-")[0]), int(assign[0].split("-")[1]) + 1))
    second_elf = set(range(int(assign[1].split("-")[0]), int(assign[1].split("-")[1]) + 1))

    if len(first_elf & second_elf) >= 1:
        pair += 1

