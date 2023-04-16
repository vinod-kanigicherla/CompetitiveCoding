# abhinav
import sys
import re

lines = [line.strip() for line in sys.stdin]
print(lines)
out = ""

for line in lines:
    n = r"[0-9]"
    numbers = re.findall(n, line)
    formatted = "({}) {}-{}".format(int("".join(numbers[0:3])), int("".join(numbers[3:6])), int("".join(numbers[6:10])))
    print(formatted)
