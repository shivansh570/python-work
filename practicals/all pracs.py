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
 
