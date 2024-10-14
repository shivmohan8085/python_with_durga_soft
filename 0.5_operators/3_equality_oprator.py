# == , != or <>

a , b, c = 10, 10, 20
x, y, z = 'hello', 'hello' , 'shiv'

print(a==b) # True
print(a==c) # False
print(a!=b) # False
print(a!=c) # True

print(x==y) # True
print(x==z) # False
print(x!=y) # False
print(x!=z) # True
# print(x<>y)  #SyntaxError: invalid syntaxs

print(10==10==10==10) # True
print('shiv'=='shiv'=='shiv'=='shiv') # True
print(10==10==10==20)  # Fslse
print('shiv'=='shiv'=='shiv'=='hello') #False   

