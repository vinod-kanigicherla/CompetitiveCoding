import sys
temp = [line.strip() for line in sys.stdin]
temp = [int(line) if line != '' else '' for line in temp]

calories_max_top = []
calories_max = 0
calories_sum = 0
for calories in temp:
    if calories == '':
        if len(calories_max_top) == 3:
            for calories_max_t in calories_max_top:
                if calories > calories_max_t:
                    calories_max_top.pop(calories_max_t)
                    calories_max.append()

        calories_max = max(calories_sum, calories_max)
        calories_sum = 0
        print(calories_max)
    else:
        calories_sum += calories

print(calories_max)