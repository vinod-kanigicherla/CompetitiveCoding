import sys
lines = [line.strip() for line in sys.stdin]
nums = []
for num in lines:
    if int(num) == 0:
        break
    else:
        nums.append(int(num))

remainders = list(map(lambda x: x%2, nums))

if all(x == remainders[0] for x in remainders):
    print("NO LIST PROBLEMS FOUND")
else:
    if remainders.count(1) > 1:
        #looking for an even
        i = remainders.index(0)
        print(str(nums[i]) + " is not odd")
    else:
        #looking for an odd
        i = remainders.index(1)
        print(str(nums[i]) + " is not even")