📝 Homework: Object-Oriented Programming (OOP) Practice
Goal: Practice using classes, inheritance, __str__, and dir() in Python.

📌 Task 1: Create a Base Class
Create a class called Person with:

name (str) and age (int) as instance variables

A method greet() that prints "Hello, my name is {name}."

A __str__ method that returns "Person(name=name, age=age)"

📌 Task 2: Inherit from the Base Class
Create a subclass called Student that inherits from Person:

Add an instance variable grade (str)

Add a method study() that prints "Student {name} is studying."

Override the __str__ method to include the grade (e.g., "Student(name=name, age=age, grade=grade)")

📌 Task 3: More Inheritance Practice
Create another subclass called Teacher that inherits from Person:

Add an instance variable subject (str)

Add a method teach() that prints "Teacher {name} is teaching {subject}."

Override the __str__ method to return "Teacher(name=name, age=age, subject=subject)"

📌 Task 4: Use the dir() Function
Write a function called show_info(obj) that:

Prints the result of dir(obj)

Prints the result of str(obj)

Call show_info() for at least one instance of Person, Student, and Teacher.

🎯 Bonus Task (Optional): Polymorphism
Write a function called introduce_people(people_list) that loops through a list of Person objects (can be Person, Student, or Teacher) and calls their greet() method. Demonstrate how different objects behave differently even though the method name is the same.

