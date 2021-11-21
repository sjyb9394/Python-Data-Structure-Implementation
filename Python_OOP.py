# Python Object-Oriented Programming

"""
Why use OOP?
- Allows us logically group our data and function and a way to easy to re-use and also easy to build upon if it needs to be.
- Data and function for specific class => attributes and method

Difference between class and instance
- Class = Simply a blueprint for creating instances
- Instance = Each unique employee(object) that we use employee class

- Constructor: Each method of class receives self instance as a first parameter automatically

- class varialbe = Variables that are shared among all instances of class while instance variable can be unique for each instance
- Class variable is accessed by instances first, if not exist, then check class itself or its parent class (such like a prototype from javascript)
- __dict__ = shows all attributes according to its object

Regular Method
- receive instance as first argument and can be accessed by instance\
- it can be called through both the class and the instance

Class Method
- simply add decorator @classmethod (cls == class)
- class method receive class as first argument instead of instances
- used when a method is not really about an instance of a class but the class itself.

use of class method
- use as a constructor

Static method
- add @staticmethod
- don't take instance or class as argument
- You do not need to access class or instance instead just call method that is in class but shares for all instances
- Has logical connection to the class but does not need a class or instance as an argument.
- Better to make sure create a static method rather than class or regular method when we are sure that we don't make use of the class or instance within the method

Inheritance
- Inherit attributes and methods from parent class
- overload = when two or more methods in one class have the same method name but different parameters
- override = when two methods have same method name and parameters but one from parent class and one from child class. Allows a child class to provide the specific implementation of a method that is already present in its parent class
- After name of the class specify which class will be inherited inside of parenthesis
- use help() to see information about attributes and methods and if it is inherited from other class
- call super().__init__ to use its parent's constructor to initiate

- isinstance() tells if the object is instance of a class
- issubclass() tells if the class is subclass of another

Special Methods (Magic/Dunder)
 - By defining our own dunder method(double underscored method), we would be able to change built-in behavior and operations
 - common methods (__repr__ and __str__)
 - __repr__ : unambiguous representation of the object and should be used for debugging and logging (seen by other developer)
 - __str__ : readable representation of an object, and used to deplay more friendly to user

Property Decorators - Getters, Setters, and Deleters
 - @property allows use as getter (shortcut for creating readonly properties)
 - @attribute_name.setter allows using as setter
 - @attribute_name.deleter allows using as deleter
"""

class Employee:
    # static variables
    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod # as a constructor
    def from_string(cls, input_string):
        first, last, pay = input_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod # static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True
    
    def __repr__(self):
        return f'Employee(\'{self.first}\', \'{self.last}\', {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email()}'
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len("".join(self.fullname().split(' ')))

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

    def prog(self):
        return self.prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def show_all_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())