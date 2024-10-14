# Logical Operators: - and , or , not

# for boolean behaviour
a = 10
b = 20
print(a>5 and b>10)  # True
print(a>100 and b>=20) # False

print(a>50 or b>10)  # True
print(a>100 or b>=200) # False

print(not(2>5)) # True


#For non-boolean types behaviour:
# x and y
'''
if x is evaluates to false return x otherwise return y
if first argument is zero then result is zero otherwise result is y  '''
print(0 and 10) # 0
print(10 and 20) #20

# x or y
'''
If x evaluates to True then result is x otherwise result is y '''
print(0 or 10) # 10
print(10 or 20) #20

print(not 20) # False
print(not 0) # True

# in strings case empty string('') means False
print('' and 'shiv')  # ''
print('shiv' and 'ram') # ram
print('' or 'shiv')  # shiv
print('shiv' or 'ram') # shiv
print(not '')  # True
print(not 'shiv')  #False
