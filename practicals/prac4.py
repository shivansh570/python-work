'''
#1) Define a class Employee that stores information about employees in the company. The class should contain the following: 
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
