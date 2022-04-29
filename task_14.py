"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Для решения создаём словарь, который будет хранить длину цепочек. В алгоритм добавим проверку на уже нахождение в вычисленной цепочке. Если так, то берём результат

NUMBER = 1_000_000 + 1
result = {}

for num in range(NUMBER):
    spam = num
    count = 0
    
    while num > 1:
        if num in result:
            count += result[num]
            break
            
        num = 3 * num + 1 if num % 2 else num / 2
        
        count += 1
                   
    result[spam] = count
        
print(max(result, key=result.get))
