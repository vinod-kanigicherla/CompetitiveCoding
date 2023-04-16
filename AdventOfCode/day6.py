import sys

temp = [line.strip() for line in sys.stdin]
print(temp)

string = temp[0]

for start in range(len(string)):
    sect = string[start:start+14]
    if len(set(sect)) == len(sect):
        print(string.index(sect) + len(sect))
        break

