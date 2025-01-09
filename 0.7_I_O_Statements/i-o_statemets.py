# x = input("First num :") # 12
# y = input("second num :") # 13 
# i = int(x)
# j = int(y)
# print(x, type(x)) #12 <class 'str'>
# print(y, type(y)) #13 <class 'str'>
# print(i + j) # 25


# # How to read multiple values from the keyboard in a single line:
# a ,b = [int(x) for x in input("Enter 2 num with space :").split()]  # 12 23
# print(a+b) # 35


# Q. Write a program to read 3 float numbers from the keyboard with , seperator and print their sum.
a, b, c = [float(x) for x in input("Enter 2 num with space :").split(",")]  # 11,23,45
print(a+b+c) # 79.0
