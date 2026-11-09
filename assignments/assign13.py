'''
#1). Create a RetailItem class with attributes: description, units_in_inventory and price.
 # Use __init__() to initialise these attributes.
 # Create three RetailItem objects with the following data:
 # 1. Jacket, 12 units, Rs. 59.95
 # 2. Designer Jeans, 40 units, Rs. 34.95
 # 3. Shirt, 20 units, Rs. 24.95

class RetailItem:
    
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price
    
    def display(self):
        print("Description:", self.description)
        print("Units in Inventory:", self.units_in_inventory)
        print("Price: Rs.", self.price)

item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95)

item1.display()
print()
item2.display()
print()
item3.display()

'''

'''
#2). Assume the RetailItem class from Q1 already exists.
 # Create a CashRegister class that maintains a list of RetailItem objects.
 # Create the following methods:
 # purchase_item(item): adds a RetailItem object to the list.
 # get_total(): returns the total price of all purchased items.
 # show_items(): displays details of all purchased items.
 # clear(): clears the list of purchased items.
 # Create a program that allows the user to select items for purchase, then displays all purchased items and the total price at checkout.


class RetailItem:

    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    def display(self):
        print("Description:", self.description)
        print("Units in Inventory:", self.units_in_inventory)
        print("Price: Rs.", self.price)


class CashRegister:

    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for i in self.items:
            total += i.price
        return total

    def show_items(self):
        for i in self.items:
            i.display()

    def clear(self):
        self.items.clear()


item1 = RetailItem("Jacket", 5, 10)
item2 = RetailItem("Jeans", 15, 20)
item3 = RetailItem("Shirt", 25, 30)

register = CashRegister()

print("AVAILABLE ITEMS")
print("1. Jacket - Rs. 10")
print("2. Jeans - Rs. 20")
print("3. Shirt - Rs. 30")
print("0. Checkout")
print("Select items to purchase by entering (1-3). Enter 0 to checkout.")

while True:
    print()
    choice = int(input("Select an item: "))

    if choice == 1:
        register.purchase_item(item1)
        print("Jacket added.")

    elif choice == 2:
        register.purchase_item(item2)
        print("Jeans added.")

    elif choice == 3:
        register.purchase_item(item3)
        print("Shirt added.")

    elif choice == 0:
        break

    else:
        print("Invalid choice!")

print()
print("PURCHASED ITEMS")
register.show_items()

print()
print("Total Price: Rs.", register.get_total())

register.clear()

'''

'''
#3). Create a Patient class with attributes for personal details, address, phone number and emergency contact. Include __init__(), getter and setter methods.
 # Create a Procedure class with attributes: procedure_name, date, practitioner and charges.
 # Include __init__(), getter and setter methods.
 # Create one Patient object with sample data and three Procedure objects:
 # 1. Physical Exam, Today's date,S Dr. Irvine, Rs. 250
 # 2. X-ray, Today's date, Dr. Jamison, Rs. 500
 # 3. Blood Test, Today's date, Dr. Smith, Rs. 200
 # Display patient details, all procedure details and total charges.

class Patient:

    def __init__(self, name, address, phone_number, emergency_contact):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact = emergency_contact

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_emergency_contact(self):
        return self.emergency_contact

    def set_emergency_contact(self, emergency_contact):
        self.emergency_contact = emergency_contact

    def display(self):
        print("Patient Name:", self.name)
        print("Address:", self.address)
        print("Phone Number:", self.phone_number)
        print("Emergency Contact:", self.emergency_contact)

class Procedure:
    
    def __init__(self, procedure_name, date, practitioner, charges):
        self.procedure_name = procedure_name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges

    def get_procedure_name(self):
        return self.procedure_name

    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_practitioner(self):
        return self.practitioner

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def get_charges(self):
        return self.charges

    def set_charges(self, charges):
        self.charges = charges

    def display(self):
        print("Procedure Name:", self.procedure_name)
        print("Date:", self.date)
        print("Practitioner:", self.practitioner)
        print("Charges: Rs.", self.charges)
    
p1 = Patient("Shivansh Singla", "Rohini, Delhi", "9876543210", "Ansh Singla")
pro1 = Procedure("Physical Exam", "2024-11-09", "Dr. Irvine", 250)
pro2 = Procedure("X-ray", "2024-11-09", "Dr. Jamison", 500)
pro3 = Procedure("Blood Test", "2024-11-09", "Dr. Smith", 200)

print("Patient Details:")
p1.display()
print()
pro1.display()
print()
pro2.display()
print()
pro3.display()
print()
total_charges = pro1.get_charges() + pro2.get_charges() + pro3.get_charges()
print("Total Charges: ", total_charges)

'''