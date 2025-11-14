# Initiate class 
class Employee:
    # Special method/Dunder method - Constructor 
    def __init__(self):
        print("This is a constructor method. It is called automatically when an object is created.")
        self.id = 123
        self.salary = 50000000
        self.role = "Data Scientist"
        print("Data/Attributes initialized.")

    def travel(self, destination):
        print("This travel function was called manually.")
        print(f"The employee is traveling to {destination}.")

# Create object/instance
sam = Employee()  # __init__() is called 
sam.name = "Sam Smith"  # Dynamic attribute assignment
print(sam.name)

# Access attributes
print(f"Employee ID: {sam.id}")
print(f"Employee Salary: {sam.salary}")
print(f"Employee Role: {sam.role}")

# Call method
sam.travel("New York")

print(type(sam))  # <class '__main__.Employee'>