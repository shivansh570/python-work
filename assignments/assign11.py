'''
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

'''

'''
#2) Suppose a dictionary named students is {"john":3, "peter":2}. What do the
following statements do?
(a) print(len(students))
(b) print(students.keys())
(c) print(students.values())
(d) print(students.items())

 a) 2
 b) ['john', 'peter']
 c) [3, 2]
 d) [('john', 3), ('peter', 2)]

'''

'''
#3) Show the output of the following code:
def main():
d = {"red":4, "blue":1, "green":14, "yellow":2}
print(d["red"])
print(list(d.keys()))
print(list(d.values()))
print("blue" in d)
print("purple" in d)
d["blue"] += 10
print(d["blue"])

ANSWERS-
 4
 ['red', 'blue', 'green', 'yellow']
 [4, 1, 14, 2]
 True
 False
 11
'''