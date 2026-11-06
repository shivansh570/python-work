'''

#1. WAP to compute the n terms of the following series: S = 1 - 2 + 3 - 4 + ...

n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i !=n:
        sum -= i
        print(f"- {i} ", end="")
    elif i % 2 != 0 and i !=n:
        sum += i
        print(f"+ {i} ", end="")
    elif i == n:
        sum += i
        print(f"+ {i} ", end="= ")
print(sum)

'''

'''

#2. WAP to compute the n terms of the following series: S = 1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
n = int(input("Enter the value of n: "))
sum = 0
for i in range(0, n + 1):
    if i == 0:
        sum += 1
        print("1 ", end="")
    elif i == 1:
        sum -= 1
        if i != n:
            print("- 1/1! ", end="")
    elif i % 2 == 0 and i != n:
        sum += 1 / factorial(i)
        print(f"+ 1/{i}! ", end="")
    elif i % 2 != 0 and i != n:
        sum -= 1 / factorial(i)
        print(f"- 1/{i}! ", end="")
    elif i == n:
        if i % 2 == 0:
            sum += 1 / factorial(i)
            print(f"+ 1/{i}! = ", end="")
        else:
            sum -= 1 / factorial(i)
            print(f"- 1/{i}! = ", end="")
print(sum)

'''