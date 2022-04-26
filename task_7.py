from math import log2

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

# Для решения используется алгоритм решето Эратосфена и Теорема о распределении простых чисел(log)


def sieve(n):
    end = int(n * log2(n) + 1)  
    sieve = [num for num in range(end)]
    sieve[0] = sieve[1] = False

    for i, num in enumerate(sieve):
        if num: 
            j = i**2 
            for k in range(j, end, i): 
                sieve[k] = False

    return [num for num in sieve if num][n - 1]


print(sieve(10_001))
