#SOLUTION 1: Seen Method
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
        seen = set()
        for num in A:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return next(iter(seen))

#SOLUTION 2: XOR Method, Nullifies Previously Seen Elements, REMEMBER, has to start with 0, works for one element
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0: return 0
    if len(A) == 1: return A[0]
    res = 0
    for num in A:
        res ^= num
    return res
