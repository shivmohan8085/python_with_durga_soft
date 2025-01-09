# -------------------- for loop ------------------------ 

# s = "Hello World"
# print(s.split())  #['Hello', 'World']
# s ="-".join(s.split())

# for i in s:
#     print(i,end="")  #Hello-World
    


# --------------- while loop ----------------
# print some of n numbers

# num = int(input("Enter num :"))
# sum, i = 0, 1 
# while i <= num:
#     sum +=i
#     i+=1
# print(f"some of {num} is : {sum}")


# infinite loop 
# while True:
#     print("**************")


#--------- star pattern -----
'''
*
**
***
****
*****
'''



# for i in range(1,6):
#     print("*"*i)


# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()


#----- using while -----
# num = 5
# i = 1
# while i <= num:
#     print("*"*i)
#     i +=1


num = 5
i = 1
while i <= num :
    j = 1
    while j <= i:
        print("*", end="") 
        j +=1
    i+=1
    print()