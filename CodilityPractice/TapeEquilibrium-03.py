# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # NOTE: Accumulating Sums from Left and Right
    lefts, rights = sum(A[:1]), sum(A[1:])
    min_diff = abs(lefts - rights)
    for i in range(1, len(A) - 1):
        lefts += A[i]
        rights-= A[i]
        min_diff = min(min_diff, abs(lefts - rights))
    return min_diff