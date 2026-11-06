'''

#1. Write a program in python to read the value of n and compute the given series: 
#   1 + 1/2 + 1/3 + ... + 1/n

n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
    if i<n:
        print(f"1/{i} + ", end="")
    else:
        print(f"1/{i} = ", end="")
print(sum)

'''

'''

#2. Write a program in python to read the value of n and compute the given series:
#   1/3 + 3/5 + 5/7 + ... + (2n-1)/(2n+1)

n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += (2 * i - 1) / (2 * i + 1)
    if i<n:
        print(f"{2*i-1}/{2*i+1} + ", end="")
    else:
        print(f"{2*i-1}/{2*i+1} = ", end="")
print(sum)

'''

'''

#3. Write a function to compute the factorial of a given number. Write a program in python
# to read the value of n and use the factorial function to compute first n terms the 
# given series: e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter the value of n: "))
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
sum = 0
for i in range(0, n + 1):
    sum += 1 / factorial(i)
    if i<n:
        print(f"1/{i}! + ", end="")
    else:
        print(f"1/{i}! = ", end="")
print(sum)

'''