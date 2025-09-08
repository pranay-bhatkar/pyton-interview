'''
🔹 Python OOP Concepts

Python is multi-paradigm, supporting both procedural and object-oriented programming. OOP revolves around objects and classes, which help organize code in a modular and reusable way.

'''


'''

1️⃣ Class and Object

Concept:

Class: A blueprint for creating objects. Defines attributes (variables) and methods (functions).

Object: An instance of a class. Each object has its own state.
'''

# Class define
class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self) :
        print(f"Car : {self.brand} {self.model}")
        
# Create object
car1 = Car("Toyota", "Corolla")
car1.display_info()


# ! Internal Working of class and objects:

# class Car: → creates a new class object of type type.

# __init__ is called automatically when object is created. Python internally calls Car.__new__() to allocate memory, then __init__() to initialize.

# self refers to the instance itself. Python stores instance attributes in __dict__ as key-value pairs.


'''
2️⃣ Encapsulation

Concept:

Encapsulation restricts direct access to some attributes/methods.

Python uses naming conventions: _protected or __private for data hiding.
'''

class Account :
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
acc = Account("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance) #   -> Error, cannot access directly

# ! Internal Working of Encapsulation:

# Python does not enforce strict private variables.

# __balance is name-mangled to _Account__balance to avoid accidental access.

# Methods access the attribute via self.__dict__.


'''
3️⃣ Inheritance

Concept:

Inheritance allows a class to reuse attributes and methods of another class.

Types: Single, Multiple, Multilevel inheritance.
'''

class Vehicle:
    def move(self):
        print("Vehicle is moving")
    
class Car(Vehicle):  # Inherits from Vehicle
    def honk(self):
        print("car honks")

c = Car()
c.move() # -> inherited
c.honk() # -> own method

# ! Internal Working of Inheritance:

# Python maintains a Method Resolution Order (MRO) using C3 linearization.

# When you call c.move(), Python searches in Car, then Vehicle.


'''
4️⃣ Polymorphism

Concept:

Polymorphism = “many forms”.

Allows same method name to behave differently depending on object.

Two types: Compile-time (Operator Overloading) and Runtime (Method Overriding).
'''

class Bird:
    def sound(self):
        print("some bird sound")
    
class Parrot:
    def sound(self):
        print("Parrot says, Hello!")

b = Bird()
p = Parrot()

b.sound()
p.sound()

# ! Internal Working Polymorphism:

# Python dynamically binds the method call to the object type at runtime.

# Function pointers in PyObject struct point to correct method.

'''
5️⃣ Abstraction

Concept:

Hides implementation details from user.

Python provides abstract base classes (ABC) in abc module.
'''

from abc import ABC , abstractmethod

class Shape(ABC) :
    @abstractmethod
    def area(slef):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
c = Circle(5)
print(c.area())

# ! Internal Working of Abstraction:

# Python marks Shape with __abstractmethods__.

# Instantiating an abstract class directly raises TypeError.

# Subclasses must override abstract methods.

'''
6️⃣ Composition vs Aggregation

Composition: Object owns another object. Lifespan tied together.

Aggregation: Object uses another object, but lifespan is independent.
'''

class Engine:
    def start(slef):
        print("Engine started")
        
class Car:
    def __init__(self):
        self.engine = Engine() # composition
    
    def start(self):
        self.engine.start()
        print("Car started")
    
car = Car()
car.start()

# ! Internal Working:

# Car object contains reference to Engine object in its __dict__.

