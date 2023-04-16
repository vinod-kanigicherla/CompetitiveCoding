a, b, c = map(int, input().split(" "))
n = 100 * a / (2*(b + (0.44 * c)))
s = f'{n:.2f}'
print(str(s) + "%")