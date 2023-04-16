# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
temp = [line.strip() for line in sys.stdin]
temp = [int(line) if line != '' else '' for line in temp]

calories_max_cache = []
calories_max = 0
calories_sum = 0
for calories in temp:
    if calories == '':
        calories_max = max(calories_sum, calories_max)
        calories_max_cache.append(calories_max)
        calories_sum = 0
    else:
        calories_sum += calories

unique_maxes = list(set(calories_max_cache))
unique_maxes.sort()
print(sum(unique_maxes[-3:]))