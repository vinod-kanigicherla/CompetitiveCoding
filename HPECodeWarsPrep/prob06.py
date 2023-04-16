
p, r, t = [float(input()) for _ in range(3)]
num = p * r * t
trunc_num = str(num).split(".")[0] + "." + str(num).split(".")[1][:2]

s_num = str(trunc_num)

if len(str(num).split(".")[-1]) == 1:
    s_num = str(num) + "0"
elif len(str(num).split(".")[-1]) == 0:
    s_num = str(num) + ".00"

print(s_num)

