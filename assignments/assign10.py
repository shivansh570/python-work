'''
#1) Write a menu driven program to perform the following on strings:
 #a) Find the length of string.

str = input("Enter a string: ")
print(f"Length of the string : {len(str)}")

'''
'''
#1) Write a menu driven program to perform the following on strings:
 #b) Return maximum of three strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str3 = input("Enter third string: ")
max = max(str1, str2, str3)
print(f"The maximum string is : {max}")

'''
'''
#1) Write a menu driven program to perform the following on strings:
 #c) Accept a string and replace all vowels with “#”.

str = input("Enter a string: ")
new_str = "" ""
for i in str:
    if i in "aeiouAEIOU":
        new_str+="#"
    else:
        new_str+=i
print(f"Modified string: {new_str}")

'''
'''
#1) Write a menu driven program to perform the following on strings:
 #d) Find number of words in the given string.

str = input("Enter a string: ")
words = str.split()
print(f"Number of words: {len(words)}")

'''
'''
#1) Write a menu driven program to perform the following on strings:
 #e) Check whether the string is a palindrome or not.

str = input("Enter a string: ")
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''

'''
#2) Write a Python program to perform the following using list: 
 #a) Check if all elements in list are numbers or not.
 #b) If it is a numeric list, then count number of odd values in it.

list = [10, 21, 30, 45, 50]
numbers = True
for x in list:
    if type(x) not in (int, float):
        numbers = False
        break
print(numbers)
if numbers:
    count = 0
    for x in list:
        if x % 2 != 0:
            count += 1
    print(count)

'''
'''
#2) Write a Python program to perform the following using list: 
 #c) If list contains all Strings, then display largest String in the list.

list = ["apple", "banana", "cherry"]
strings = True
for x in list:
    if type(x) != str:
        strings = False
        break
if strings:
    largest_string = list[0]
    for x in list:
        if x > largest_string:
            largest_string = x
    print(largest_string)

'''
'''
#2) Write a Python program to perform the following using list: 
 #d) Display list in reverse form.

list = [10, 20, 30, 40]
reversed = list[::-1]
print(reversed)

'''
'''
#2) Write a Python program to perform the following using list: 
 #e) Find a specified element in list.

list = [10, 20, 30, 40]
element = 30
found = -1
for i in range(len(list)):
    if list[i] == element:
        found = i
        break
print(found)

'''
'''
#2) Write a Python program to perform the following using list:
 #f) Remove the specified element from the list.

list = [10, 20, 30, 40]
element = 30
newlist = []
for x in list:
    if x != element:
        newlist.append(x)
print(newlist)

'''
'''
#2) Write a Python program to perform the following using list:
 #g) Sort the list in descending order.

list = [40, 10, 30, 20]
list.sort(reverse=True)
print(list)

'''
'''
#2) Write a Python program to perform the following using list:
 #h) Accept 2 lists and find the common members in them.

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
print(common)

'''

'''

#3) Use dictionary to store marks of the students in 4 subjects. Write a function to find the name of the student securing highest percentage.

students = {"a": 85,"b": 92,"c": 78,"d": 95}
highest = 0
top = ""
for name in students:
    marks = students[name]
    if marks > highest:
        highest = marks
        top = name
print(top)

'''