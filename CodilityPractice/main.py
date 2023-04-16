# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if len(A) == 0: return A
    K = K % len(A) #SO SMART, remainder is the simplified rotations
    return A[-K:] + A[:-K]
