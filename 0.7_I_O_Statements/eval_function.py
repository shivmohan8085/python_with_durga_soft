# The eval() function in Python is used to evaluate a string as a Python expression and return the result of the expression.
# eval(expression, globals=None, locals=None)

# def add(a, b):
#     return a + b
# result = eval('add(5, 3)')
# print(result)  # Output: 8

print(eval("10+23"))  # 33

i = eval(input("enter a list :"))
print(i, type(i))

'''
enter a list :[1,2.3,4]
[1, 2.3, 4] <class 'list'>
or 
enter a list :11,23,45,56,13,4
(11, 23, 45, 56, 13, 4)
'''
