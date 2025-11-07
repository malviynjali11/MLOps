# Initiate a class - 
class Employee:
    # special method/magic also called dunder mothod - Constructor
    def __init__(self):
        print("Started executing attributes/data .")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data have been initiated .")

    def travel(self, destination):
        print("This travel function was called manually .")
        print(f"Employee is traveling to {destination} .")

# create an object/instance of the class
sam = Employee()

# Printing the attributes of the object
# print(sam.salary)
# Calling the method 
# sam.travel("New Delhi")
print(type(sam)) # <class '__main__.Employee'>  
