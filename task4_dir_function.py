#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Task 4: Use the dir() Function
Date: May 8, 2025

======================================================================
📌 Task 4: Use the dir() Function
======================================================================
Write a function called show_info(obj) that:
- Prints the result of dir(obj)
- Prints the result of str(obj)
- Call show_info() for at least one instance of Person, Student, and Teacher.
"""
from task1_base_class import Person
from task2_inheritance import Student
from task3_more_inheritance import Teacher
def show_info(obj):
    return dir(obj)