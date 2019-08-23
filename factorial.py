# return.single.value.2.py
from functools import reduce
from operator import mul

# def factorial(n):
#     return reduce(mul, range(1, n + 1), 1)

# print(mul(2,3))

# f5 = factorial(5)  # f5 = 120

# def imprime(x, y):
#     return "x " + str(x) + " y " + str(y)

print(reduce(lambda x, y: x*y, range(1,6), 1))

def factorial(n):
    if n in (0,1):
        return 1
    else:
        return factorial(n-1) * n

f5 = factorial(5)  # f5 = 120
print("Resultado do factorial: ", f5)