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