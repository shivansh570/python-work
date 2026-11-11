'''

#4). Create an Employee class with attributes name and employee number.
 # Create a ProductionWorker subclass with shift number (1 = Day, 2 = Night)
 # and hourly pay rate.
 # Add appropriate accessor and mutator methods to both classes.
 # Create a ProductionWorker object, accept its details from the user,
 # and display them using accessor methods.
    

class Employee:

    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def get_name(self):
        return self.name

    def get_employee_number(self):
        return self.employee_number

    def set_name(self, name):
        self.name = name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number


class ProductionWorker(Employee):

    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.shift_number

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

name = input("Enter employee name: ")
employee_number = input("Enter employee number: ")
shift_number = int(input("Enter shift number (1 for Day, 2 for Night) : "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))

worker = ProductionWorker(name, employee_number, shift_number, hourly_pay_rate)

print()
print("Employee Details-")
print("Employee Name:", worker.get_name())
print("Employee Number:", worker.get_employee_number())
print("Shift Number:", worker.get_shift_number())

if worker.get_shift_number() == 1:
    print("Shift: Day")
elif worker.get_shift_number() == 2:
    print("Shift: Night")

print("Hourly Pay Rate: Rs.", worker.get_hourly_pay_rate())

'''

'''
#2). Generate all prime numbers from 1 to 30 and store them in a text file named "Prime",
 # with each number on a separate line.
 # Open the file for reading and display its contents using:
 # 1. read()
 # 2. readline()
 # 3. readlines()


file = open("Prime.txt", "w")

for num in range(2, 31):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        file.write(str(num) + "\n")

file.close()

print("Method 1 (read):")
print()
file = open("Prime.txt", "r")
print(file.read())
file.close()

print("Method 2 (readline):")
print()
file = open("Prime.txt", "r")
print(file.readline())
for i in file:
    print(i)
file.close()

print("Method 3 (readlines):")
print()
file = open("Prime.txt", "r")
print(file.readlines())
file.close()


'''