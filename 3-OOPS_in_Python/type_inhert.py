#........................................... Single or Basic Inheritance....................................

# In single inheritance, a class (child class) inherits from one parent class.
# This allows the child class to access methods and attributes of the parent class.
class Parent:
    def __init__(self):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")
# Create an instance of the Child class
child = Child("Alice")
child.greet()  # Inherited method from Parent class
child.play()   # Method from Child class
# Output:
# Hello, my name is Alice.
# Alice is playing.

#........................................... Multi-Level Inheritance....................................
# In multi-level inheritance, a class inherits from a child class, which in turn inherits from a parent class.
class Grandparent:
    def __init__(self, name):
        self.name = name
    def tell_story(self):
        print(f"{self.name} is telling a story.")
# Intermediate class inheriting from Grandparent
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working.")
# Deriving class inheriting from Parent
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of the Child class
child = Child("Bob")
child.tell_story()  # Inherited from Grandparent
child.work()        # Inherited from Parent
child.play()        # Method from Child class
# Output:
# Bob is telling a story.
# Bob is working.
# Bob is playing.

#........................................... Hierarchical Inheritance....................................
# In hierarchical inheritance, multiple child classes inherit from a single parent class.
class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")
# First child class inheriting from Parent
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")
# Second child class inheriting from Parent
class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying.") 
# Create instances of Child1 and Child2
child1 = Child1("Charlie")
child2 = Child2("Diana")
child1.greet()  # Inherited from Parent
child1.play()   # Method from Child1
child2.greet()  # Inherited from Parent
child2.study()  # Method from Child2
# Output:
# Hello, my name is Charlie.
# Charlie is playing.
# Hello, my name is Diana.
# Diana is studying.

#........................................... Multiple Inheritance (Diamond Problem)....................................
# In multiple inheritance, a class can inherit from more than one parent class.
class A:
    def __init__(self, name):
        self.name = name 
    def greet(self):
        print(f"Hello from A, my name is {self.name}.")
class B(A):
    def greet(self):
        print(f"Hello from B, my name is {self.name}.")
        super().greet()
class C(A):
    def greet(self):
        print(f"Hello from C, my name is {self.name}.")
        super().greet()
class D(B, C):
    def greet(self):
        print(f"Hello from D, my name is {self.name}.")
        super().greet()

# Create an instance of class D
d = D("Eve")    
d.greet()  # Method resolution order will determine which greet() methods are called        
# Output:
# Hello from D, my name is Eve.
# Hello from B, my name is Eve.
# Hello from C, my name is Eve.
# Hello from A, my name is Eve.

# .....................................................Hybrid Inheritance....................................
# Hybrid inheritance is a combination of two or more types of inheritance.
class Animal:
    def __init__(self, name):
        self.name = name 
    def sound(self):
        print(f"{self.name} makes a sound.")
# Intermediate class1
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")
# Intermediate class2
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")
# Derived class inheriting from both Mammal and Bird
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name) # Explicit call to constructor of Mammal
    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")  
bat.sound()    # Inherited from Animal
bat.feed()     # Inherited from Mammal
bat.fly()      # Inherited from Bird
bat.nocturnal() # Method from Bat class
# Output:
# Bruce makes a sound.
# Bruce is feeding milk.
# Bruce is flying.
# Bruce is nocturnal.
        