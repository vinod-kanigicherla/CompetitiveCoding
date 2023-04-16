#Sieve of Erastothenes

n = 5 #number to check if prime


def is_prime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
