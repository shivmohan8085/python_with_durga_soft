# arithmatic operators are +, -, * , /, //, %,**
a = 10
b = 2
print(a+b) # 12
print(a-b) # 8
print(a*b) # 20
print(a/b) # 5.0
print(a%b) # 0
print(a**b)  #100
print(a//b) # 5
#but 
print(10.0//2)  #5.0
print(10/2.0) # 5.0

'''
Note: / operator always performs floating point arithmetic. Hence it will always returns 
float value.
But Floor division (//) can perform both floating point and integral arithmetic. If 
arguments are int type then result is int type. If atleast one argument is float type then 
result is float type.
'''

# We can use +,* operators for str type also.
a = 'hello '
b = 'world'
print(a+b) # hello world
print('hello ' * 2) # hello hello