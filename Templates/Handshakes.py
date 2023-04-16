handshakes = 0
def recursive(n): #n couples
    if n == 0:
        return
    global handshakes
    handshakes += 4 * n
    recursive(n - 1)

recursive(4)
print(handshakes)