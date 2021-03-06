"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Классический перебор чисел a и b и поиск c через условие равенста суммы 1 000. При этом согласно свойствам Пифагоровых троек одно из чисел кратно 3, а другое 4, поэтому и шаг такой.
"""

RESULT = 1_000
A = 3
B = 4
for a in range(A, RESULT, A):
    for b in range(B, RESULT - a, B):
        c = RESULT - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c) 
            break   
       
"""
Решение через формулу Эвклида для генерации троек: a=m^2-n^2, b=2mn, c=m^2+n^2. При условии, что a+b+c = 1000, m и n не могут быть больше 21-25 где-то
"""

for m in range(21):
    for n in range(21):
        if m >= n:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c == 1000:
                print(a * b * c)
                
