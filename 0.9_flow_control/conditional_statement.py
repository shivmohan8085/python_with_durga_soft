# name = input("Enter Your Name :")
# if name == "Shiv":
#     print(f"hello {name} Good Morning")


# if name == "Raj":
#     print(f"hello {name} Good Afternoon")
# else:
#     print(f"Hello {name} How Are you")


data = input("Enter some data (int, string, or bool): ")

if data.isdigit():
    print("The entered data is of type 'int'.")
elif data.lower() == 'true' or data.lower() == 'false':
    print("The entered data is of type 'bool'.")
else:
    print("The entered data is of type 'string'.")


'''
Enter some data (int, string, or bool): 11
The entered data is of type 'int'.

Enter some data (int, string, or bool): true
The entered data is of type 'bool'.

Enter some data (int, string, or bool): hello
The entered data is of type 'string'
'''