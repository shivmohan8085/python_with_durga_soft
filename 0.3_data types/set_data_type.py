s = {10,10,20,3,'shiv','Shiv'}

print(s)
for i in s:print(i, end=' ') # 3 shiv 20 Shiv 10

# print(s[0]) #TypeError: 'set' object is not subscriptable

s.add(100)
print(s)
s.remove('Shiv')
print(s)