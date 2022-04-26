"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Решение через поиск НОК разложением на простые множители: берём уникальные максимальные степени множителя
К примеру 8 = 2^3
Чтобы не перебирать числа и раскладывать на множители, просто проверял возведением в степень
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]

total = 1

for num in primes:
    if num**4 >= 20:
        if num**3 >= 20:
            if num**2 >= 20:
                total *= num
            else:
                total *= num**2
        else:
            total *= num**3
    else:
        total *= num**4
        
print(total)
