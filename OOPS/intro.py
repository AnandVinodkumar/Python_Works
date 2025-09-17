# Object Oriented Programming
#======================================

# Class >> Blueprint for creating more than one object

# Object >> Creating objects using the class (blueprint)

# Methods >> Defined in a class which can be executed only by the object of that class


class Details:  # Creating a class named Details

    def method1(self):  # Defining a method inside the class (can be executed only by the object of that class)
        
        print("Method called successfully")

object1 = Details()  # Creating an object of the class Details

object1.method1()  # Calling the method using the object of the class


# Advantages
#=========================

# Inheritance
"""
A class (Child/Subclass) to inherit attributes and methods from another class (Parent/Superclass)
"""

# class Parent:   # Super-class, Parent Class

#     def car(self):

#         print("Maruthi")

#     def bike(self):

#         print("Splendor")

# class Child(Parent):    # Sub-class, Derived class

#     pass


# user1 = Parent()

# user2 = Child()

# user2.bike()


# Types
# Single inheritence
# Multi-level inheritence
# Multiple inheritence
# Hierarchical
# Hybrid


"""Multi-level"""
class Grandfather:

    def asset(self):

        print("Owns Property")

class Father(Grandfather):

    def business(self):

        print("Run business")

class Grandson(Father):

    def job(self):

        print("Working in IT")

obj1 = Grandson()
obj1.asset()
obj1.business()
obj1.job()
#============================

"""Multiple"""
class Grandfather:

    def asset(self):

        print("Owns Property")

class Father:

    def business(self):

        print("Run business")

class Grandson(Father,Grandfather):

    def job(self):

        print("Working in IT")

obj1 = Grandson()
obj1.asset()
obj1.business()
obj1.job()
#======================================


# Encapsulation :The Bundling of data and methods in a single unit

# Abstraction: Hiding complex implementation details and showing only necessary details

class A:

    def method1(self):

        print("hello") 

user1 = A()

# Polymorphism
# ==================

# Method overriding
# Subclass provides a specific implementation of a method that is already defined in its parent class.

# Method Overloading

class Parent:

    def method1(self):

        print("hello")

class Child(Parent):

    def method1(self):

        print("hello")