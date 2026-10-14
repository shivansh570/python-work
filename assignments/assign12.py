'''
#1. Write a function to create a list having n integer elements. Write another function where list is passed as parameter and it counts the number of occurrences of each element of the list.

n = int(input("enter the number of elements in the list: "))
def create(n):
    l = []
    for i in range(n):
        l.append(int(input("enter an integer: ")))
    return l

def count(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

lst = create(n)
print(lst)
print(count(lst))

'''

'''
#2. Write a program that reads numbers separated by commas in one line and stores the distinct numbers in a list.

line = input("Enter numbers separated by commas: ")
lst = [int(x) for x in line.split(",")]
distinct = list(set(lst))
print("Distinct numbers:", distinct)

'''

'''
#3. Write a python program/statement to interchange the first and last element in the list

lst = [10, 20, 30, 40, 50]
lst[0], lst[-1] = lst[-1], lst[0]
print("Updated list: ", lst)

'''

'''
#4. Using list comprehension create a list having only even numbers from the given list - [1,4,3,2,6,3,7,8,10,3,3].


L1 = [1, 4, 3, 2, 6, 3, 7, 8, 10, 3, 3]
L2 = [i for i in L1 if i % 2 == 0]
print("Even numbers list:", L2)

'''

'''
#5. given the list - [1, 4, 3, 2, 6, 3, 7, 8, 10, 3, 3].
 #a) Multiply all numbers in the list
 #b) program to find smallest number in a list without using Function
 #c) program to remove Nth occurrence of the given element

#a)-
lst = [1, 4, 3, 2, 6, 3, 7, 8, 10, 3, 3]
prod = 1
for i in lst:
    prod *= i
print("Product of all numbers:", prod)

#b)- 
my_list = [1, 4, 3, 2, 6, 3, 7, 8, 10, 3, 3]
smallest = my_list[0]
for i in my_list:
    if i < smallest:
        smallest = i
print("Smallest number is:", smallest)

#c)-
lst = [1, 4, 3, 2, 6, 3, 7, 8, 10, 3, 3]
element = 3 #let our target be 3
n = 3 #let n = 3(third occurence )
count = 0
for i in range(len(lst)):
    if lst[i] == element:
        count += 1
        if count == n:
            lst.pop(i)
            break 
print(f"List after removing the {n}rd occurrence of {element}: {lst}")

'''