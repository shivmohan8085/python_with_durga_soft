# sep: Determines what goes between values in a print() call.
# end: Determines what is printed at the end of the print() call (default is a newline \n).

# print('shiv', 'mohan', sep='-')
# print('Shiv', end=', ')
# print('Mohan', end='. \n')
# print('Python', 'java', 'Ruby', sep='| ', end='.')

'''
shiv-mohan
Shiv, Mohan.
Python| java| Ruby.

'''


# In Python, the .format() method allows you to format strings in a more readable and flexible way than using string concatenation. It can be used with print() to insert values into a string at specified positions.

print("value of a = {} and value of b ={}".format(10,20))
print("value of a = {0} and value of b ={1}".format(10,20))
print("value of a = {1} and value of b ={0}".format(10,20))
print("value of a = {x} and value of b ={y}".format(x = 100, y=200))
print("value of a = {y} and value of b ={x}".format(x = 100, y=200))

x = 300
y = 4000
print("value of a ={x} and value of b ={y}")
print(f"value of a = {x} and value of b = {y}")

'''
value of a = 10 and value of b =20
value of a = 10 and value of b =20
value of a = 20 and value of b =10
value of a = 100 and value of b =200
value of a = 200 and value of b =100
value of a ={x} and value of b ={y}
value of a = 300 and value of b = 4000

'''