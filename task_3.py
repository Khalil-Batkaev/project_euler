"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

"""
Решение через решето Эратосфена не оптимальное в плане слишком большого количества неиспользуемых простых чисел.
Сделал через проверку на простоту перебором делителей. Дальше идёт разложение числа на простые множители
"""


def check_prime(number):
    if number in {2, 3}:
        return True
    max_div = int(number ** 0.5) + 1
    
    for div in range(2, max_div, 2):
        is_prime = True
        if not number % div:
            is_prime = False
            break
    
    return is_prime


num = 600_851_475_143
limit = int(num**0.5)
divisors = []

for div in range(2, limit):
    if check_prime(div) and not num % div:
        divisors.append(div)
        num /= div
    if num == 1:
        break
     
print(divisors[-1])
