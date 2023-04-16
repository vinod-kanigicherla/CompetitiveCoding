# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    distance = Y - X
    steps = distance // D
    if distance % D > 0: steps += 1
    return steps