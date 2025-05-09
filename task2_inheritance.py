#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Task 2: Inherit from the Base Class
Date: May 8, 2025

======================================================================
📌 Task 2: Inherit from the Base Class
======================================================================
Create a subclass called Student that inherits from Person:
- Add an instance variable grade (str)
- Add a method study() that prints "Student {name} is studying."
- Override the __str__ method to include the grade
  (e.g., "Student(name=name, age=age, grade=grade)")
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f" Hello my name is {self.name}")
    def __str__(self):
        return f"Person (name={self.name}, age{self.age})"
class Student(Person):
    def __init__(self, name, age,grade):
        self.grade=grade
        super().__init__(name, age)
    def study(self):
        return f"Student {self.name} is studying."
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
b=Student('malika',13,50)
b.greet()
print(b)
