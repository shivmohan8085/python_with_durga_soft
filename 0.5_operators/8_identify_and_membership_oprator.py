'''
We can use identity operators for address comparison.
2 identity operators are available
1. is 
2. is not
r1 is r2 returns True if both r1 and r2 are pointing to the same object
r1 is not r2 returns True if both r1 and r2 are not pointing to the same object
'''
a = 10
b = 10
c = a+b
d = 20
print(a is b) # True
print(a==b)  # True
print(c is d)  # True
print(c==d)  # True
print(a is not b) # False
print(c is not d) # False


s = 'shiv'
s1 = 'shiv'
print(s is s1) # True

l = ['ram', 2, 3, 'jay']
l2 = ['ram', 2, 3, 'jay']
print(l is l2)  # False
print(id(l)) # 2505270941952
print(id(l2)) # 2505270940032

print(l == l2) # True

'''
Note:
We can use is operator for address comparison where as == operator for content 
comparison.'''

# membership oprator 
str1 = 'shivmohan'
print('sh' in str1) # True
print('n' in str1) # True

my_list = ['shiv',12,33,1.6]
print(1.6 in my_list) # True
print('shiv' not in my_list) # False
