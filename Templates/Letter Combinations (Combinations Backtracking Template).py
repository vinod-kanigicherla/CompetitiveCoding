from string import ascii_letters as letters

n, k = map(int, input().split())

possibilities = list(letters[:n])

def combinations(possibilities, k, res=[]):
    if len(res) == k:
        print("".join(res))
        return

    for i, possibility in enumerate(possibilities):
        res.append(possibility)
        combinations(possibilities[i + 1:], k, res)
        res.pop()

combinations(possibilities, k)

