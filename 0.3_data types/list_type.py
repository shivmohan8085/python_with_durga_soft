# 1. insertion order is preserved
# 2. heterogeneous objects are allowed
# 3. duplicates are allowed
# 4. Growable in nature
# 5. values should be enclosed within square brackets.

l = [1,"shiv", 12.02, True,1+5j, 0b1010 ] 
print(l)  # [1,"shiv", 12.02, True,1+5j, 0b1010 ]
print(l[0])  #1
l.append(1)
print(l)
l.remove(l[1])
l.remove(1)
print(l)

