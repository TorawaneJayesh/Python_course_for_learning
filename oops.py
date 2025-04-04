# """ 
#     Object oriented programming (oop) - oop in python is a way of writing code using object and classes.
    
#     class - a  blueprint for creating objects. class name first letter is capital.
    
#     object - a specific instance of a class with its own data and behavior.
    
#      encapsulation - keeping details hidden and allowing only necessary access. ex. a mobile phone hides its internal 
#      circuits and lets you use only buttons and the screen.
     
#      inheritance - a new thing (class) getting features from an existing thing. ex. a "SportsCar" class inherits from
#      the "Car" class but adds extra speed.
     
#      polymorphism - the same action can happens in different ways. ex. a dog and cat both make sounds but a dog 
#      barks and cat meows.
     
#      absraction - showing only important details and hiding the rest. ex. when driving a car you just use the 
#      steering wheel not the engine's inner workings.
     
     
# """

# # create a class 
# class Car:
#     def __init__(self, brand, model): # here init is constructur and brand and models are attributes.
#         self.brand = brand
#         self.model = model
#     def show_details(self):# method function
#         print(f"car:{self.brand} model {self.model}")
        
# # create a object
# my_car1 = Car("tata", "range rover")
# my_car2 = Car("mahindra", "thar")

# # call a object method
# my_car1.show_details()
# my_car2.show_details()
# #del my_car2   this is used for delete a object
# my_car2.show_details() 

# # now we are creating a class student
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def show_details(self):
#         print(f"student name {self.name} get {self.marks} marks")

# s1 = Student("jayesh", 12)
# s2 = Student("shahu", 23)

# s1.show_details()
# s2.show_details()


# # here is a real life example of class world
# class World:
#     planet = "earth" # this is a class attribute
#     def __init__(self, animal, plant):
#         self.animal = animal
#         self.plant = plant
#     def information(self):
#         print(f"{self.animal} is animal and {self.plant} is plant both are live on {self.planet}")

# obj1 = World("tiger", "grapes") # this is a object attribute
# obj2 = World("human", "banian tree")

# obj1.information()
# obj2.information()

# class Hospital:
#     hname = "MBBS Clinic"
#     def __init__(self, pname, plocation, pdoctor):
#         self.pname = pname
#         self.plocation = plocation
#         self.pdoctor = pdoctor
#     def hdata(self):
#         print(f"patient name is {self.pname} he is from {self.plocation} and his doctor is {self.pdoctor} in our {self.hname}")

# p1 = Hospital("jayesh", "chougaon", "mule")
# p1.hdata()

# # input object from user

# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
#     def display(self):
#         print(f"{self.name} = {self.marks}")
#     @staticmethod # this is a statik method it use for not use self parameter.
#     def college():
#         print("New college")
# def get_data():
#     students = []
#     n = int(input("enter how many student: "))
#     for i in range(n):
#         name = input("enter student name: ")
#         marks = int(input(f"enter {name}'s mark: "))
#         students.append(Student(name, marks))
#     return students
# students = get_data()
# for student in students:
#     student.display()
#     student.college()
    
# # create object using function   

# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
        
#     def dis(self):
#         print(f"car model is {self.model} and its prince is {self.price}")
    
# def car_info():
#     cars = []
#     cars.append(Car("car1","1"))
#     cars.append(Car("car2","2"))
#     return cars
# cars = car_info()
# for car in cars:
#     car.dis()


# # polynorphism  - class different but method same.
# # method overiding (means file ko firse write karna.)
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def sound(self):
#         print(f"{self.name} is bark")
# class Cat:
#     def __init__(self ,name):
#         self.name= name
#     def sound(self):
#         print(f"{self.name} is meaw")
# s1 = Dog("dog")
# s2 = Cat("cat")
# for i in (s1, s2):
#     i.sound()

# encapsulation (data hiding).
# data ko private banana taki sidhe acceses na kar sake (use __ double underscore before attribute.)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance # privete attribute
#     def get_balance(self):
#         return self.__balance # safe acceses method
# account = BankAccount(5000)
# print(account.get_balance())

# # inheritance
# # ek class dusri class class ki properties aur methods ko use kar sakti hai.
# # here dog is a child class which is inherit from animal class
# class Animal: # parent class
#     def speaks(self):
#         print("animal speaks.")
# class Dog (Animal): # child class
#     def bark(self):
#         print("dog barks.")
# dog = Dog()
# dog.speaks() # from parent class
# dog.bark() # from child class


# # super method (it is use to acceses methods of parent class)
# class Animal: # parent class
#     def __init__(self, name):
#         self.name = name
#     def speaks(self):
#         print("animal speaks.")
# class Dog (Animal): # child class
#     def bark(self):
#         print("dog barks.")
#         super().speaks() 
#         super().__init__(print(self.name)) # init fun = is use to acceses attribute of parent class
# dog = Dog("tommy")
# dog.bark()



# abstraction (hide implementation)
# sirf jaruri details dikhana baki hide karna.

# from abc import ABC, abstractmethod
# class Shape(ABC):# abstract class 
#     @abstractmethod
#     def area(self):
#         pass 
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# c = Circle(5)
# print("circle area:",c.area())










