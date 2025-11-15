# Object Oriented programming: Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

#A class defines what an object should look like, and an object is created based on that class.

#Self is a conventionally used parameter that refers to the instance of a class within the class's methods. It is the first parameter that every instance method of a class must take.

'''Constructor is a special method that is automatically called when a new instance (object) of a class is created. Its main purpose is to initialize the attributes of the newly created object. [ eg: __init__() ]
Types of constructors:
# A default constructor does not take any parameters other than self. It initializes the object with default attribute values.
# A parameterized constructor accepts arguments to initialize the object's attributes with specific values.  '''

class Score:
    def __init__(self, name, marks, result, grade=12):
        self.name = name
        self.marks = marks
        self.result = result
        self.grade = grade

    def score_card(self):
        print(f'{self.name}, The student of class {self.grade} has got {self.marks}% in class 12 and therefore {self.name} is considered {self.result}')

student1 = Score("Arin Sharma", "65", "Passed")
student2 = Score("Advik Verma", "69", "Passed")

student1.score_card()
student2.score_card()

'''
The four pillars of Object-Oriented Programming (OOP) in Python are: 
#Encapsulation: Bundling data and methods, protecting data within objects.
#Inheritance: Creating new classes based on existing ones, promoting code reuse.
#Polymorphism: Allowing objects to take on multiple forms, enabling flexible method calls.
#Abstraction: Hiding complex implementation details, showing only essential features.'''

#Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador): 
    def guide(self):
        print(f"{self.name} Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print(f"{self.name} barks")


lab = Labrador("Max")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Cookie")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Coco")
retriever.display_name()
retriever.greet()
retriever.sound()


#Polymorphism
class Calculator:
    def add(self, *num):
        return sum(num)
    
Sum = Calculator()
print(Sum.add(5, 10, 45, 67))     
print(Sum.add(5, 10, 1, 5, 9)) 
print(Sum.add(1, 2, 3)) 


#Encapsulation
class Dog:
    def __init__(self, name, breed, age):
        self.name = name 
        self._breed = breed 
        self.__age = age 

    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


dog = Dog("Buddy", "Labrador", 3)

print(dog.name)
print(dog._breed) 
print(dog.get_age())
dog.set_age(9)
print(dog.get_info())

#Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print('Bike color is blue')

class Car(Vehicle):
    def start(self):
        print('Car color is red')

bike = Bike()
car = Car()

bike.start()
car.start()