# range( start_index , end_index , step)  # end index is always excluded

r = range(10)
print(type(r)) # <class 'range'>
print(r[0]) # 0


r1 = range(0,10,2)
print(r1[1]) # 2

r3 = range(10,1,-1)
print(r3[0])  # 10


for i in range(10):print(i ,end=' ')  # 0 1 2 3 4 5 6 7 8 9  # by default start index is 0 and step is 1+
for i in range(2,21,2):print(i, end=' ') #  2 4 6 8 10 12 14 16 18 20

l = list(range(1,11))
print(l) # [1, 2, 3, 4, 5   , 6, 7, 8, 9, 10]

