
# int to string
s = '10'
print(type(s))  # <class 'str'>
y = int(s)
print(type(y)) #<class 'int'>


# float to int
f = 20.10
g = int(f)
print(g)

# # but
# f1 = '20.10'
# g1 = int(f1)  # ValueError: invalid literal for int() with base 10: '20.10'
# print(g)   

# bool to string
x = True
y = False
print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>

print(type(int(x))) #<class 'int'>
print(type(int(y))) # <class 'int'>





# # complex to int
# com = 2_5j
# print(int(com))   #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


# str1 = 'ten'
# print(int(str1))  # ValueError: invalid literal for int() with base 10: 'ten'


# binary to int
b = 0b1111
print(int(b))  # 15