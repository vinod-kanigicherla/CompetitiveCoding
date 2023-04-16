# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    curr, max_cnt, found_one = 0, 0, False
    while N:
        if N & 1 == 1:
            if found_one is False:
                found_one = True
            else:
                max_cnt = max(curr, max_cnt)
            curr = 0
        else:
            curr += 1
        N >>= 1
    return max_cnt
