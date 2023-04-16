import sys

cake = [list(line.strip()) for line in sys.stdin][1:]

def solve(n):
    solutions = []
    state = set()
    search(state, solutions, n)
    return solutions

def is_valid_state(state):
    #checking if it is a valid solution
    return check2x2()
    True

def get_candidates(state):
    return []

def search(state, solutions, n):
    if is_valid_state(state):
        solutions.append(state.copy())
        #return
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)
