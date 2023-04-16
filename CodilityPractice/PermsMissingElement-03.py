# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0: return 1
    n = len(A) + 1
    #math formaula for summation of series from 1 to n
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(A)
