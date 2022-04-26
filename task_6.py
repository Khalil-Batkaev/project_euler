"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

"""
Для решения используется формула для рсчёта суммы последовательных натуральных чисел: n(n+1)/2
и её модификация для квадратов: n(n+1)(2n+1)/6
"""

MAX_NUMBER = 100

sum_squares = int(MAX_NUMBER * (MAX_NUMBER + 1) * (2 * MAX_NUMBER + 1) / 6)
square_sum = int((MAX_NUMBER * (MAX_NUMBER + 1) / 2)**2)

print(square_sum - sum_squares)
