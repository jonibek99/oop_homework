#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Task 3: More Inheritance Practice
Date: May 8, 2025

======================================================================
📌 Task 3: More Inheritance Practice
======================================================================
Create another subclass called Teacher that inherits from Person:
- Add an instance variable subject (str)
- Add a method teach() that prints "Teacher {name} is teaching {subject}."
- Override the __str__ method to return "Teacher(name=name, age=age, subject=subject)"
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f" Hello my name is {self.name}"
    def __str__(self):
        return f"Person (name={self.name}, age{self.age})"
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject
    def teach(self):
        return f"Teacher {self.name} is teaching {self.subject}."
    def __str__(self):
        return f"Teacher(name={self.name}, age={self.age}, subject={self.subject})"
c=Teacher('Dilfuza',54,'English')
print(c.teach())
 