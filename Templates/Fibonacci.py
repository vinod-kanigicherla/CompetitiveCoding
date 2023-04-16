fib_list = []
a, b = 1, 1
n = 10 # given n fibonacci nums to print

for i in range(n):
    fib_list.append(a)
    a, b = b, a + b