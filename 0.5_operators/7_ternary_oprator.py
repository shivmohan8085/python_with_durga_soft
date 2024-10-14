'''
x = firstValue if condition else secondValue
If condition is True then firstValue will be considered else secondValue will be considered.

Note: Nesting of ternary operator is possible.
'''
a = 10
b = 20
max = a if a>b else b
print(max) # 20

x= int(input("First num :"))
y= int(input("second num :"))
z= int(input("third num :"))
max = x if x>y and x>z else y if y>z else z  
min = x if x<y and x<z else y if y<z else z  

print('max value is :', max)
print('min value is :', min)
