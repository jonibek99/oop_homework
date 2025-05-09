#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Task 1: Create a Base Class
Date: May 8, 2025

======================================================================
📌 Task 1: Create a Base Class
======================================================================
Create a class called Person with:
- name (str) and age (int) as instance variables
- A method greet() that prints "Hello, my name is {name}."
- A __str__ method that returns "Person(name=name, age=age)"
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f" Hello my name is {self.name}"
    def __str__(self):
        return f"Person (name={self.name}, age={self.age})"
a=Person('ali',13)
print(a.greet())

