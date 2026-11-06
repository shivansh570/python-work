#1) Define a class Employee that stores information about employees in the company. The class should contain the following: 
 #(i) data members- count (to keep a record of all the objects being created for this class) and for every employee: an employee number, Name, Dept, Basic, DA and HRA.                                   
 #(ii) function members: 
  #a. __init__ method to initialize and/or update the members. Add statements to ensure that the program is terminated if any of Basic, DA and HRA is set to a negative value. 
  #b. function salary, that returns salary as the sum of Basic, DA and HRA. 
  #c. __del__ function to decrease the number of objects created for the class. 
  #d. __str__ function to display the details of an employee along with the salary of an employee in a proper format.