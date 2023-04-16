import sys
num = float([line.rstrip() for line in sys.stdin][0])
ld = int(str(num)[-1])

if ld == 7:
    num += 0.02
elif ld % 2 == 1:
    num -= 0.09
elif ld > 7:
    num -= 4.00
elif ld < 4:
    num += 6.78

s_num = str(num)

if len(str(num).split(".")[-1]) == 1:
    s_num = str(num) + "0"
elif len(str(num).split(".")[-1]) == 0:
    s_num = str(num) + ".00"

print(s_num)