'''
#1). Write a program to find the roots of a quadratic equation.

a = float(input("enter the coefficient of x^2: "))
b = float(input("enter the coefficient of x: "))
c = float(input("enter the constant: "))

if a != 0:
  D = b**2 - 4 * a * c
  if D >= 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(f"Roots of the equation are: {x1} and {x2}")
  else:
    print("The equation has no real roots (complex roots).")
else:
  print("Error: Coefficient of x^2 must be non-zero.")

'''

'''
#2). Write a program to accept a number ‘n’ and
 #a. Check if ’n’ is prime
 #b. Generate all prime numbers till ‘n’
 #c. Generate first ‘n’ prime numbers

n = int(input("enter a number :"))

def prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def all_prime(n):
    lis = [ ]
    for i in range(2,n+1):
        if prime(i):
           lis.append(i)
    return lis

def first_primes(n):
  lis = [ ]
  c = 0
  num = 2
  while c < n:
    if prime(num):
      c += 1
      lis.append(num)
    num += 1
  return lis

if prime(n):
  print(f"{n} is a prime number.")
else:
  print(f"{n} is not a prime number.")

print(f"Prime numbers till {n}: \n {all_prime(n)}")

print(f"First {n} prime numbers: \n {first_primes(n)}")

'''

'''
#3). Write a program to create a pyramid of the character ‘*’ and a reverse pyramid

n = int(input("enter the number of lines of pyramid : "))

print("\nPyramid:")
for i in range(1, n + 1):
  spaces = " " * (n - i)
  stars = "*" * (2 * i - 1)
  print(spaces + stars)

print("\nReverse Pyramid:")
for i in range(n, 0, -1):
  spaces = " " * (n - i)
  stars = "*" * (2 * i - 1)
  print(spaces + stars)

'''

'''
#4). Write a program that accepts a character and performs the following:
 #a. print whether the character is a letter or numeric digit or a special character.
 #b. if the character is a letter, print whether the letter is uppercase or lowercase.
 #c. if the character is a numeric digit, prints its name in text.

char = input("enter character: ")

def type_char(char):
  if char.isalpha():
    print(f"{char} : is a letter.")
  elif char.isdigit():
    print(f"{char} : is a digit.")
  else:
    print(f"{char} : is a special character.")


def type_case(char):
  if char.isalpha():
    if char.islower():
      print(f"{char} : is lowercase")
    else:
      print(f"{char} : is uppercase")


def numeric_text(char):
  if char.isdigit():
    D = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE"}
    print(f"{char} : {D[char]}")

type_char(char)
type_case(char)
numeric_text(char)

'''

'''
#5). Write a program to perform the following operations on a string:
 #a. Find the frequency of a character in a string.
 #b. Replace a character by another character in a string.
 #c. Remove the first occurrence of a character from a string.
 #d. Remove all occurrences of a character from a string.

text = input("Enter string: ")

def frequency(text):
  s = input("Enter character to count: ")
  print(f"{text.count(s)} : is the number of times '{s}' is present in the string.")

def replace_char(text):
  s1 = input("Enter character to replace: ")
  s2 = input("Enter new character: ")
  print(f"{text.replace(s1, s2)} : is the new string.")

def remove_first_occur(text):
  s1 = input("Enter character to remove (first occurrence): ")
  print(f"{text.replace(s1, '', 1)} : is the new string.")

def remove_all_occur(text):
  s1 = input("Enter character to remove (all occurrences): ")
  print(f"{text.replace(s1, '')} : is the new string.")

frequency(text)
replace_char(text)
remove_first_occur(text)
remove_all_occur(text)

'''

'''
#6). Write a program to swap the first n characters of two strings.

str1 = input("enter string : ")
str2 = input("enter string : ")
n = int(input("enter number of characters to switch"))
print(f"new str1 : {str2[:n] + str1[n:]}")
print(f"new str2 : {str1[:n] + str2[n:]}")

'''

'''
#7). Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list.If the second string is not present in the first string then it should return -1.

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
#8). Write a program to create a list of the cubes of only the even integers appearing in the input list (may have elements of
#other types also) using the following: 
 #a. 'for' loop 
 #b. list comprehension

L1= [ ] 
while True:
    a = int(input("Enter number : "))
    L1.append(a)
    g = input("cont? (y/n)")
    if g.lower() !="y":
        break

L2 = [ ]
for i in L1:
    if i%2==0:
        L2.append(i**3)
print(L2)

L3 = [x*x*x for x in L1 if x%2==0]
print(L3)

'''

'''
#9). Write a program to read a file and:
 # a. Count the total number of characters, words and lines.
 # b. Count the frequency of each character using a dictionary.
 # c. Print the words in reverse order.
 # d. Copy even-numbered lines to "File1" and odd-numbered lines to "File2".

file = open("File.txt", "r")
data = file.read()
file.close()

print("Total Characters:", len(data))
print("Total Words:", len(data.split()))
print("Total Lines:", len(data.splitlines()))

frequency = {}
for ch in data:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print("\nCharacter Frequency:")
print(frequency)

words = data.split()
print("\nWords in Reverse Order:")
print(" ".join(words[::-1]))

file = open("File.txt", "r")
data = file.readlines()
file.close()
file1 = open("File1.txt", "w")
file2 = open("File2.txt", "w")
for i in range(len(data)):
    if (i+1) % 2 == 0:
        file1.write(data[i])
    else:
        file2.write(data[i])
file1.close()
file2.close()

'''

'''
#10). Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys.

def cube():
    dict = {x: x**3 for x in range(1, 6)}
    print(dict)
cube()

'''

'''
#11). Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following operations: 
 #a. Print half the values of the tuple in one line and the other half in the next line. 
 #b. Print another tuple whose values are even numbers in the given tuple. 
 #c. Concatenate a tuple t2=(11,13,15) with t1. 
 #d. Return maximum and minimum value from this tuple.

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

half_len = len(t1) // 2
print(t1[:half_len])
print(t1[half_len:])

t3 = tuple(x for x in t1 if x % 2 == 0)
print(t3)

t2 = (11, 13, 15)
t4 = t1 + t2
print(t4)

print("Maximum value:", max(t1))
print("Minimum value:", min(t1))

'''

'''
#12) Define a class Employee that stores information about employees in the company. The class should contain the following: 
 #(i) data members- count (to keep a record of all the objects being created for this class) and for every employee: an employee number, Name, Dept, Basic, DA and HRA.                                   
 #(ii) function members: 
  #a. __init__ method to initialize and/or update the members. Add statements to ensure that the program is terminated if any of Basic, DA and HRA is set to a negative value. 
  #b. function salary, that returns salary as the sum of Basic, DA and HRA. 
  #c. __del__ function to decrease the number of objects created for the class. 
  #d. __str__ function to display the details of an employee along with the salary of an employee in a proper format.

class Employee:
    count = 0 

    def __init__(self, emp_number, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise ValueError("Basic, DA, and HRA must be non-negative values.")
        self.emp_number = emp_number
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.count += 1  

    def salary(self):
        return self.basic + self.da + self.hra  

    def __del__(self):
        Employee.count -= 1  

    def __str__(self):
        return (f"Employee Number: {self.emp_number}\n"
                f"Name: {self.name}\n"
                f"Department: {self.dept}\n"
                f"Basic: {self.basic}\n"
                f"DA: {self.da}\n"
                f"HRA: {self.hra}\n"
                f"Salary: {self.salary()}")

e1 = Employee(101, "Shiv", "IT", 30000, 5000, 3000)
e2 = Employee(102, "ansh", "CS", 25000, 4000, 2000)

print(e1)
print()
print(e2)
print()
print("Total Employees:", Employee.count)

'''

'''
#13). Write a program to define a class "2DPoint" with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point2D(3, 4)
p2 = Point2D(6, 8)
print(p1)
print()
print(p2)
print(f"Distance between {p1} and {p2}: {p1.distance(p2)}")

'''

'''
#14). Inherit the Point2D class to create a Point3D class with an additional attribute z. 
 # Override the distance() method to calculate the distance between two 3D points. Create objects and display them.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Point3D(Point2D):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 +
                (self.y - point.y) ** 2 +
                (self.z - point.z) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"
    
p1 = Point3D(3, 4, 5)
p2 = Point3D(6, 8, 9)

print(p1)
print()
print(p2)

print("Distance between", p1, "and", p2, ":", p1.distance(p2))

'''

'''
#15). Accept a name from the user, then-
 # Raise and handle appropriate exceptions if the entered text contains digits and/or special characters.

try:
    name = input("Enter your name: ")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Invalid name")

except ValueError:
    print("Name should contain only alphabets.")

else:
    print("Name:", name)

'''