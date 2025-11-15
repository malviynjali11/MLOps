# # Simple Inheritance 

# # Base Class 
# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived Class

# class Dog(Animal):
#     def __init__(self):
#         self.behavior = "friendly"
#     def speak(self):
#         print(f"Cherruu barks. And she is {self.behavior}.")

# # # Create an instance of Animal 
# # animal = Animal("Genric Animal")
# # animal.speak() #O/P: Genric Animal makes a sound.

# # Create an instance of dog 
# dog = Dog()
# dog.speak() #O/P: Cherry barks.

#.............................................SUPER..................................................

# Base Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # Call the constructor of the base class
        self.breed = breed
    def speak(self):
        super().speak()  # Call the speak method of the base class
        print(f"{self.name} barks and is a {self.breed}.")

# Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# O/P:
# Buddy makes a sound.
# Buddy barks and is a Golden Retriever.
        