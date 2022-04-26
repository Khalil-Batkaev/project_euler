"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
Собираем множество чисел из кратных 3, потом кратных 5. Далее считаем сумму
"""

END = 1000
NUM1 = 3
NUM2 = 5

numbers = {num for num in range(NUM1, END, NUM1)}

for num in range(NUM2, END, NUM2):
    numbers.add(num)
 
print(sum(numbers))    
