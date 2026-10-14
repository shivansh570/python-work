#1) Write a function to create a dictionary having character as the key and value as the number of occurrences of the character in the string passed as parameter.

s = input("enter a string: ")
def count(s):
    d = { }
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
print(count(s))