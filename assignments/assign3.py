'''
#1. Write a Python Program to print the Pattern: 
 # 1
 # 1 2
 # 1 2 3
 # 1 2 3 4
 # 1 2 3 4 5

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''

'''
#2. Write a Python Program to print the Pattern:
 # 1 2 3 4 5
 # 1 2 3 4 
 # 1 2 3
 # 1 2
 # 1 

n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):   
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''

'''
#3. write a Python Program to print the Pattern:
 #         1
 #       2 1
 #     3 2 1
 #   4 3 2 1
 # 5 4 3 2 1

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

'''

