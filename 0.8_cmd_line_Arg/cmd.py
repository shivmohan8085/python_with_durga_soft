# import sys
# print(type(sys.argv)) #<class 'list'>

# from sys import argv
# print(type(argv)) #<class 'list'>

# print(argv)

'''
d:/Python_Exercise/python_with_durga_soft/0.8_cmd_line_Arg/cmd.py shiv ram yes
<class 'list'>
<class 'list'>
['d:/Python_Exercise/python_with_durga_soft/0.8_cmd_line_Arg/cmd.py', 'shiv', 'ram', 'yes']
'''

# from sys import argv
# arg = argv[1:]
# x = 0
# for i in arg:
#     x += int(i)
# print(x)

'''
d:/Python_Exercise/python_with_durga_soft/0.8_cmd_line_Arg/cmd.py 10 20 23
53
'''

# from sys import argv
# arg = argv[1:]
# print(arg)

'''
 d:/Python_Exercise/python_with_durga_soft/0.8_cmd_line_Arg/cmd.py 'shiv bhatt' 'mohan yadav' "rahul sharma"
['shiv bhatt', 'mohan yadav', 'rahul sharma']

'''

from sys import argv
print(argv[1]+argv[2]) # 2344
print(int(argv[1])+int(argv[2])) #67

'''
 d:/Python_Exercise/python_with_durga_soft/0.8_cmd_line_Arg/cmd.py 23 44                                    
2344
67
'''