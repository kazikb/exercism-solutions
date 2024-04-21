# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
# Opis algorytmu na wiki:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def primes(limit):
    prime = [True for i in range(limit + 1)]

    p = 2
    while p * p <= limit:
        if prime[p] == True:
            for i in range(p*p, limit+1, p):
                prime[i] = False
        p += 1

    return [n for n in range(2, limit+1) if prime[n] == True]
