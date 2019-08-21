from math import factorial

integer = int(input("Qual numero inteiro voce quer transformar? "))
binario = bin(integer)
hexa = hex(integer)

dividendo = 7
divisor = 2

print("Inteiro: ", integer)
print("Binario: ", binario)
print("Hexadecimal: ", hexa)

res1, res2 = divmod(dividendo, divisor)

print("res1 ", res1)
print("res2 ", res2)

print(factorial(5))
