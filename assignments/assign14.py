'''
#1). Create a Pet class with private attributes __name, __animal_type and __age.
 # Use __init__() to initialise them.
 # Create setter methods: set_name(), set_animal_type(), set_age().
 # Create getter methods: get_name(), get_animal_type(), get_age().
 # Create a program that takes the pet's name, type and age as input,
 # creates an object and displays the details using getter methods.

class Pet:

    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_animal_type(self, type):
        self.__animal_type = type

    def get_animal_type(self):
        return self.__animal_type

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

Name = input("Enter the name of the pet: ")
Type = input("Enter the type of the pet: ")
Age = int(input("Enter the age of the pet: "))

a1 = Pet(Name, Type, Age)

print("Pet Name:", a1.get_name())
print("Pet Type:", a1.get_animal_type())
print("Pet Age:", a1.get_age())

'''

'''
#2). Create a Car class with private attributes __year_model, __make and __speed.
 # Initialise year_model and make using __init__(), and set speed to 0.
 # Create accelerate() to increase speed by 5, brake() to decrease speed by 5,
 # and get_speed() to return the current speed.
 # Create a Car object, call accelerate() 5 times and display the speed after
 # each call. Then call brake() 5 times and display the speed after each call.

class Car:

    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
    
    def  brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed

car1 = Car(2020, "Toyota")

for i in range(5):
    car1.accelerate()
    print("Current speed after accelerating:", car1.get_speed())

for i in range(5):
    car1.brake()
    print("Current speed after braking:", car1.get_speed())

'''

'''
#3). Create an Employee class with attributes: name, ID number, department and job title.
 # Use __init__() to initialise these attributes.
 # Create three Employee objects with the following data:
 # 1. Susan Meyers, 47899, Accounting, Vice President
 # 2. Mark Jones, 39119, IT, Programmer
 # 3. Joy Rogers, 81774, Manufacturing, Engineer
 # Display the details of all three employees.

class Employee:

    def __init__(self, user, id_number, dept, title):
        self.user = user
        self.id_number = id_number
        self.dept = dept
        self.title = title
    
    def display(self):
        print("Employee Name:", self.user)
        print("Employee ID:", self.id_number)
        print("Employee Department:", self.dept)
        print("Employee Title:", self.title)

e1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
e2 = Employee("Mark Jones", 39119, "IT", "Programmer")
e3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")   

e1.display()
print()
e2.display()
print()
e3.display()

'''


