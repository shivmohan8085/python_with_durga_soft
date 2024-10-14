'''
These operators are applicable only for int and boolean types.
By mistake if we are trying to apply for any other type then we will get Error. '''

# & | ^ ~ << >>
print(4&5)  # 4
# print(10.05 & 2.7) #TypeError: unsupported operand type(s) for &: 'float' and 'float'

# but
print((3.5 < 5) & (3 < 5.6))  # True
print((3.5 > 5) | (3 < 5.6))  # True
print((3.5 > 5))

'''
& If both bits are 1 then only result is 1 otherwise result is 0
| If atleast one bit is 1 then result is 1 otherwise result is 0
^ If bits are different then only result is 1 otherwise result is 0
~ bitwise complement operator i.e 1 means 0 and 0 means 1
>> Bitwise Left shift Operator
<< Bitwise Right shift Operator '''


print(4^5) # 1
'''
binary of 4 - 0100
binary of 5 - 0101
            --------
               0001    that means decimal or 0001 is 1 
'''

#  ~ complemt rule ~x = -(x+1)
print(~12) # -13

print(10 << 2) # 40
'''
binary of 10 in 8 digits  =>  00001010
shift 2 place in left side => 00101000  - in decimal 40
'''

print(10 >> 2) # 2
'''
binary of 10 in 8 digits  =>  00001010
shift 2 place right side => 00000010  - in decimal 2
'''


