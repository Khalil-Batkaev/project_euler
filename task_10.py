"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# Для решения используется алгоритм решето Эратосфена
def sieve(n):
    end = n + 1
    sieve = [num for num in range(end)]
    sieve[0] = sieve[1] = False

    for i, num in enumerate(sieve):
        if num: 
            j = i**2 
            for k in range(j, end, i): 
                sieve[k] = False

    return sum([num for num in sieve if num])


print(sieve(2_000_000))
