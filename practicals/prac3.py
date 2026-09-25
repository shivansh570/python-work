'''
#1. Write a program that accepts a character and performs the following:
#a)	print whether the character is a letter or numeric digit or a special character.
char = input('enter character: ')
if char.isalpha():
    print(f"{char} : is a letter.")
elif char.isdigit():
    print(f"{char} : is a digit.")
else:
    print(f"{char} : is a special character.")

'''
'''
#1. Write a program that accepts a character and performs the following:
#b) if the character is a letter, print whether the letter is uppercase or lowercase
char = input('enter character: ')
if char.isalpha():
    if char.islower():
        print(f"{char} : is lowercase")
    else:
        print(f"{char} : is uppercase")

'''
'''
#1. Write a program that accepts a character and performs the following:
#c) if the character is a numeric digit,
 #prints its name in text (e.g., if input is 9, output is NINE) 
char = input('enter character: ')
if char.isdigit():
    D = {0 : "ZERO", 1 : "ONE", 2 : "TWO", 3 : "THREE", 4 : "FOUR", 5 : "FIVE",
        6 : "SIX", 7 : "SEVEN", 8 : "EIGHT", 9 : "NINE"}
    print(D[int(char)])

'''

'''
#2. Write a program to perform the following operations on a string:
 #a) Find the frequency of a character in a string.
str = input("enter string : ")
s = input("enter text to count : ")
print(f"{str.count(s)} : is the number of times the text is present in string")

'''
'''
#2. Write a program to perform the following operations on a string:
 #b) Replace a character by another character in a string. 
str = input("enter string : ")
s1 = input("enter text to replace: ")
s2 = input("enter new text : ")
print(f"{str.replace(s1,s2)} : is the new string.")

'''
'''
#2. Write a program to perform the following operations on a string:
 #c) Remove the first occurrence of a character from a string. 
str = input("enter string : ")
s1 = input("enter text to remove: ")
print(f"{str.replace(s1, "", 1)} : is the new string.")

'''
'''
#2. Write a program to perform the following operations on a string:
 #d) Remove all occurrences of a character from a string.
str = input("enter string : ")
s1 = input("enter text to remove: ")
print(f"{str.replace(s1, "")} : is the new string.")

'''

'''
#3. Write a program to swap the first n characters of two strings.
 
str1 = input("enter string : ")
str2 = input("enter string : ")
n = int(input("enter number of characters to switch"))
print(f"new str1 : {str2[:n] + str1[n:]}")
print(f"new str2 : {str1[:n] + str2[n:]}")

'''

'''
#4) Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list.If the second string is not present in the first string then it should return -1.

str1 = input("enter string : ")
str2 = input("enter string : ")

def occur(str1,str2):
    if str2 not in str1:
        return -1
    else:
        list = [ ]
        st = 0
        for i in range(len(str1)):
            index = str1.find(str2, st)
            if index == -1:
                break
            list.append(index)
            st = index + 1
        return(list)
print(occur(str1,str2))

'''

'''
#5) Write a program to read a string with multiple lines and:
 #a) Print the total number of characters, words and lines in the string.
str = input("enter texts, use '\\n' for different lines : ")
lines = len(str.split("\\n"))
newstr = str.replace('\\n' , ' ')
words = len(newstr.split())
chars = len(newstr)
print(f"Total Lines: {lines}")
print(f"Total Words: {words}")
print(f"Total Characters: {chars}")

'''
'''
#5) Write a program to read a string with multiple lines and:
 #b) Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.
str = input("enter texts, use '\\n' for different lines : ")
newstr = str.replace("\\n", "")
char = {}
for i in newstr:
    if i not in char:
        char[i] = 1
    else:
        char[i] = char[i] + 1
print(f"Character Frequencies: {char}")

'''
'''
#5) Write a program to read a string with multiple lines and:
# c) Print the words in reverse order. 
str = input("enter texts, use '\\n' for different lines : ")
list = str.replace("\\n", " ").split()
list = list[::-1]
words = " ".join(list)
print(f"Words in reverse order: {words}")

'''
'''
#5) Write a program to read a string with multiple lines and:
 #d) Copy even lines of the string to a string named ‘str1’ and odd lines to another string named ‘str2’.
str = input("enter texts, use '\\n' for different lines : ")
list = str.split('\\n')
list1 , list2 = [ ] , [ ]
for i in range(len(list)):
    if i%2==0:
        list1.append(list[i])
    else:
        list2.append(list[i])
str1 = ' '.join(list1)
str2 = ' '.join(list2)
print(f"str1 : {str1}")
print(f"str2 : {str2}")

'''

'''
#6) Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys.
 # also, store the data in a string and perform the operations given in the question.

def cube():
    dict = {x: x**3 for x in range(1, 6)}
    str1 = str(dict)
    print(str1)
cube()

'''