# bin() :-  We can use bin() to convert from any base to binary
# oct() :-  We can use oct() to convert from any base to octal
# hex() :- We can use hex() to convert from any base to hexa decimal

print(bin(10)) # 0b1010
print(oct(0b1010)) #0o12
print(bin(0o12)) #0b1010
print(hex(0b1010)) #0xa
print(bin(0xa)) #0b1010
print(oct(0xa)) #0o12

from math import * 
print(factorial(5))