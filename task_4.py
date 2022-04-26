"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Через методы строк находим палиндром и проверём его на кратность числам от 100 до 999


def get_palindrome():
    MIN_NUMBER = 100
    MAX_NUMBER = 999
    START = MAX_NUMBER**2
    
    for num in range(START, 0, -1):
        if str(num) == (str(num))[::-1]:
            for div in range(MAX_NUMBER, MIN_NUMBER, -1):
                if not num % div and MIN_NUMBER <= num / div <= MAX_NUMBER:
                    return num


print(get_palindrome())
