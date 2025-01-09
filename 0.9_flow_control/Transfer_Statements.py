# Break

# d = {123: "Raju", 124: "Amit", 125: "Sita", 126: "John", 127: "Priya", 128: "Rahul", 129: "Neha", 130: "Arjun", 131: "Meena", 132: "Ravi"}
# for emp_id, emp_name in d.items():
#     if emp_name == "Priya":
#         print(f"Priya is found with ID {emp_id}")
#         break
#         print("--->")



# continue

# d = {123: "Raju", 124: "Amit", 125: "Sita", 126: "John", 127: "Priya", 128: "Rahul", 129: "Neha", 130: "Arjun", 131: "Meena", 132: "Ravi"}
# for emp_id, emp_name in d.items():
#     if emp_name == "Priya" or emp_name == "Raju":
#         continue
#     print(f"{emp_name} is found with ID {emp_id}")

data = int(input("enter any number: "))
for i in range(1,data+1):
    if i % 2==0:
        continue
    else:
        print(i, end=" ")

'''
enter any number: 50
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49

'''